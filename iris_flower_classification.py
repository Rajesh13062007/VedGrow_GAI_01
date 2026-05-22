import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print(df.head())
print(df.info())
print(df.describe())
print(df["species"].value_counts())

sns.countplot(data=df, x="species")
plt.title("Count of Iris Species")
plt.show()

sns.pairplot(df, hue="species", vars=iris.feature_names)
plt.show()

sns.heatmap(df[iris.feature_names].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

X = df[iris.feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(kernel="rbf", random_state=42)
}

trained_models = {}
results = []

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    trained_models[model_name] = model
    y_pred = model.predict(X_test_scaled)

    results.append({
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1-Score": f1_score(y_test, y_pred, average="weighted")
    })

    print("\\n", "=" * 60)
    print(f"Classification Report for {model_name}")
    print("=" * 60)
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=iris.target_names,
                yticklabels=iris.target_names)
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted Species")
    plt.ylabel("Actual Species")
    plt.show()

results_df = pd.DataFrame(results)
print(results_df)

def predict_iris_species(sepal_length, sepal_width, petal_length, petal_width, model_name="SVM"):
    custom_input = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=iris.feature_names
    )
    custom_input_scaled = scaler.transform(custom_input)
    prediction = trained_models[model_name].predict(custom_input_scaled)[0]
    return iris.target_names[prediction]

print("Custom Prediction:", predict_iris_species(5.1, 3.5, 1.4, 0.2, "SVM"))