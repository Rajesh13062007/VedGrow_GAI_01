# Iris Flower Classification

This project is completed for the VedGrow Generative AI Internship task.

## Task Objective

Train and evaluate classification models on the classic Iris dataset.

## Dataset

The Iris dataset contains flower measurements for three Iris species:

- Setosa
- Versicolor
- Virginica

Features used:

- Sepal length
- Sepal width
- Petal length
- Petal width

## Models Used

This project trains and compares three machine learning models:

1. K-Nearest Neighbors (KNN)
2. Decision Tree Classifier
3. Support Vector Machine (SVM)

## Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Project Files

```text
VedGrow_GAI_01/
│
├── Iris_Flower_Classification.ipynb
├── README.md
└── requirements.txt
```

## How to Run

1. Clone this repository or download the files.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Open the notebook:

```bash
jupyter notebook Iris_Flower_Classification.ipynb
```

4. Run all cells from top to bottom.

## Custom Prediction Example

The notebook includes a section to predict the Iris species for custom input values:

```python
custom_input = [[5.1, 3.5, 1.4, 0.2]]
```

The model will return the predicted species name.

## Author

Rajesh A
