# Prompt Engineering Showcase

**Task 1 - VedGrow Generative AI Internship**

## Objective

This document demonstrates 25 effective prompts across five domains: coding, writing, summarization, analysis, and creative work. Each example includes a bad prompt, an optimized prompt, and the reasoning behind the improvement.

## Prompt Types Covered

- **Zero-shot prompting:** Asking the model to perform a task without examples.
- **Few-shot prompting:** Providing examples so the model can follow the desired pattern.
- **Reasoning-summary prompting:** Asking the model to solve step by step internally and provide a concise explanation or key steps, rather than asking for hidden chain-of-thought.

## Domains Covered

1. Coding
2. Writing
3. Summarization
4. Analysis
5. Creative

---

## Prompt 1: Python Bug Fixing

**Domain:** Coding  
**Prompt Type:** Zero-shot  
**Use Case:** Debugging Python code with explanation.

### Bad Prompt

```text
Fix this code.
```

### Optimized Prompt

```text
You are a Python debugging assistant. Review the code below, identify the error, explain the cause briefly, and provide a corrected version. Also mention one best practice to avoid this issue in the future.

Code:
```python
# paste code here
```
```

### Why This Is Better

Adds role, context, specific output structure, and a learning goal.

---

## Prompt 2: SQL Query Generation

**Domain:** Coding  
**Prompt Type:** Few-shot  
**Use Case:** Generating SQL queries from natural language.

### Bad Prompt

```text
Write SQL for sales.
```

### Optimized Prompt

```text
Convert the user request into a SQL query. Follow the examples.

Example 1:
Request: Show total sales by month.
SQL: SELECT DATE_TRUNC('month', order_date) AS month, SUM(amount) AS total_sales FROM orders GROUP BY month ORDER BY month;

Example 2:
Request: Show the top 5 customers by revenue.
SQL: SELECT customer_id, SUM(amount) AS revenue FROM orders GROUP BY customer_id ORDER BY revenue DESC LIMIT 5;

Now write SQL for this request:
Request: Show average order value by product category for 2025.
```

### Why This Is Better

Provides examples, expected style, and schema assumptions, improving accuracy.

---

## Prompt 3: Algorithm Explanation

**Domain:** Coding  
**Prompt Type:** Reasoning summary  
**Use Case:** Learning an algorithm.

### Bad Prompt

```text
Explain binary search.
```

### Optimized Prompt

```text
Explain binary search for a beginner. Include: purpose, step-by-step process, Python implementation, time complexity, and one simple example trace. Keep the explanation clear and concise.
```

### Why This Is Better

Specifies audience, structure, code language, and required complexity details.

---

## Prompt 4: Code Review

**Domain:** Coding  
**Prompt Type:** Zero-shot  
**Use Case:** Improving code quality.

### Bad Prompt

```text
Review my code.
```

### Optimized Prompt

```text
Act as a senior software reviewer. Review the code below for readability, performance, security, and maintainability. Return your answer in four sections: strengths, issues, suggested improvements, and improved code.

Code:
```
# paste code here
```
```

### Why This Is Better

Transforms a vague request into a structured review with criteria.

---

## Prompt 5: Regex Creation

**Domain:** Coding  
**Prompt Type:** Few-shot  
**Use Case:** Creating useful regular expressions.

### Bad Prompt

```text
Make regex for emails.
```

### Optimized Prompt

```text
Create a regular expression based on the examples.

Positive examples: user@example.com, rajesh.a@domain.co.in
Negative examples: user@@example.com, rajesh@, domain.com

Task: Create a regex for valid basic email addresses and explain what each part does.
```

### Why This Is Better

Few-shot examples clarify the boundary between valid and invalid outputs.

---

## Prompt 6: Professional Email

**Domain:** Writing  
**Prompt Type:** Zero-shot  
**Use Case:** Writing workplace emails.

### Bad Prompt

```text
Write leave email.
```

### Optimized Prompt

```text
Write a polite professional email requesting one day of leave. Include a clear subject line, greeting, reason, date of leave, assurance about pending work, and closing. Tone: respectful and concise.
```

### Why This Is Better

Adds tone, parts of the email, and purpose.

---

## Prompt 7: LinkedIn Post

**Domain:** Writing  
**Prompt Type:** Few-shot  
**Use Case:** Creating professional social media posts.

### Bad Prompt

```text
Write LinkedIn post.
```

### Optimized Prompt

```text
Write a LinkedIn post in the style of these examples.

Example tone: professional, grateful, learning-focused, not overly dramatic.
Example structure: achievement, task details, skills learned, thanks, hashtags.

Now write a LinkedIn post about completing an Iris Flower Classification machine learning project using KNN, Decision Tree, and SVM. Include a placeholder for the GitHub link.
```

### Why This Is Better

Gives style guidance and content requirements, making the output ready to use.

---

## Prompt 8: Resume Bullet Improvement

**Domain:** Writing  
**Prompt Type:** Reasoning summary  
**Use Case:** Improving resume content.

### Bad Prompt

```text
Improve this resume point.
```

### Optimized Prompt

```text
Improve the resume bullet below using action verbs, measurable impact, and concise language. Briefly explain why the new version is stronger.

Original bullet: Worked on machine learning project.
```

### Why This Is Better

Defines the improvement criteria and requests a short explanation.

---

## Prompt 9: Formal Report Intro

**Domain:** Writing  
**Prompt Type:** Zero-shot  
**Use Case:** Writing project report sections.

### Bad Prompt

```text
Write introduction.
```

### Optimized Prompt

```text
Write a 150-word introduction for a project report on prompt engineering. Include the importance of prompts, applications in AI tools, and the goal of building a reusable prompt library. Tone: academic but simple.
```

### Why This Is Better

Adds length, topic scope, required points, and tone.

---

## Prompt 10: Tone Rewriting

**Domain:** Writing  
**Prompt Type:** Few-shot  
**Use Case:** Adapting tone for communication.

### Bad Prompt

```text
Make it better.
```

### Optimized Prompt

```text
Rewrite the message in three tones: professional, friendly, and concise.

Original message: I cannot come today because I have other work.

Return the answer in a table with columns: Tone and Rewritten Message.
```

### Why This Is Better

Clear transformation instructions and format reduce ambiguity.

---

## Prompt 11: Article Summary

**Domain:** Summarization  
**Prompt Type:** Zero-shot  
**Use Case:** Summarizing articles.

### Bad Prompt

```text
Summarize this.
```

### Optimized Prompt

```text
Summarize the text below in 5 bullet points. Then provide a 2-sentence overall summary and list 3 important keywords.

Text:
[paste text here]
```

### Why This Is Better

Specifies length, format, and additional keyword extraction.

---

## Prompt 12: Meeting Notes Summary

**Domain:** Summarization  
**Prompt Type:** Few-shot  
**Use Case:** Creating meeting minutes.

### Bad Prompt

```text
Summarize meeting notes.
```

### Optimized Prompt

```text
Convert meeting notes into structured minutes. Use this format:

Title:
Date:
Attendees:
Key Discussion Points:
Decisions Made:
Action Items with Owner and Deadline:

Notes:
[paste notes here]
```

### Why This Is Better

Provides a reusable format for practical meeting documentation.

---

## Prompt 13: Research Paper Summary

**Domain:** Summarization  
**Prompt Type:** Reasoning summary  
**Use Case:** Understanding research papers.

### Bad Prompt

```text
Explain this paper.
```

### Optimized Prompt

```text
Summarize the research paper text for a beginner. Include: problem statement, method, dataset/tools, key findings, limitations, and practical applications. Keep technical terms simple and briefly explain necessary terms.
```

### Why This Is Better

Breaks a complex task into focused sections and defines the target audience.

---

## Prompt 14: Long-to-Short Summary

**Domain:** Summarization  
**Prompt Type:** Zero-shot  
**Use Case:** Shortening long content.

### Bad Prompt

```text
Make this shorter.
```

### Optimized Prompt

```text
Condense the text below to under 100 words while preserving the main message, important facts, and original meaning. Avoid adding new information.

Text:
[paste text here]
```

### Why This Is Better

Adds word limit and prevents hallucinated additions.

---

## Prompt 15: Book/Chapter Summary

**Domain:** Summarization  
**Prompt Type:** Few-shot  
**Use Case:** Academic study notes.

### Bad Prompt

```text
Summarize chapter.
```

### Optimized Prompt

```text
Summarize the chapter using this structure:
1. Main idea
2. Key events or arguments
3. Important terms
4. Lessons learned
5. 5-question quiz with answers

Chapter text:
[paste text here]
```

### Why This Is Better

Turns summary into a study resource with comprehension checks.

---

## Prompt 16: Data Insight Analysis

**Domain:** Analysis  
**Prompt Type:** Zero-shot  
**Use Case:** Business data interpretation.

### Bad Prompt

```text
Analyze this data.
```

### Optimized Prompt

```text
Analyze the table below and identify the top 5 insights. For each insight, include supporting evidence from the data and a possible business recommendation.

Table:
[paste table here]
```

### Why This Is Better

Defines insight count, evidence requirement, and action-oriented output.

---

## Prompt 17: SWOT Analysis

**Domain:** Analysis  
**Prompt Type:** Few-shot  
**Use Case:** Business/project evaluation.

### Bad Prompt

```text
Do SWOT.
```

### Optimized Prompt

```text
Create a SWOT analysis for the given business idea. Use four sections: Strengths, Weaknesses, Opportunities, and Threats. Add 4 points under each section.

Business idea: An AI-powered study planner app for college students.
```

### Why This Is Better

Specifies framework and number of points, improving completeness.

---

## Prompt 18: Decision Matrix

**Domain:** Analysis  
**Prompt Type:** Reasoning summary  
**Use Case:** Tool comparison and decision-making.

### Bad Prompt

```text
Which option is better?
```

### Optimized Prompt

```text
Compare the following options using a decision matrix. Criteria: cost, ease of use, scalability, learning value, and risk. Score each criterion from 1 to 5 and briefly justify each score. End with a recommendation.

Options: ChatGPT, Gemini, Claude
```

### Why This Is Better

Uses a structured evaluation method and asks for evidence-based recommendation.

---

## Prompt 19: Root Cause Analysis

**Domain:** Analysis  
**Prompt Type:** Zero-shot  
**Use Case:** Troubleshooting technical problems.

### Bad Prompt

```text
Why did this fail?
```

### Optimized Prompt

```text
Perform a root cause analysis for the issue below. Use the 5 Whys method, list the likely root cause, and suggest 3 preventive actions.

Issue: A machine learning model performs well on training data but poorly on testing data.
```

### Why This Is Better

Specifies an analytical method and desired solution output.

---

## Prompt 20: Pros and Cons

**Domain:** Analysis  
**Prompt Type:** Few-shot  
**Use Case:** Evaluating educational technology.

### Bad Prompt

```text
Tell pros cons.
```

### Optimized Prompt

```text
Analyze the pros and cons of using AI tools for student learning. Return the answer as a table with columns: Aspect, Pros, Cons, and Balanced Recommendation. Include at least 5 aspects.
```

### Why This Is Better

Changes a broad opinion request into a balanced structured analysis.

---

## Prompt 21: Story Idea

**Domain:** Creative  
**Prompt Type:** Zero-shot  
**Use Case:** Generating story concepts.

### Bad Prompt

```text
Give story.
```

### Optimized Prompt

```text
Create a short story idea about a student who builds an AI assistant. Include genre, main character, conflict, twist, and ending. Keep it original and suitable for a general audience.
```

### Why This Is Better

Specifies creative elements and audience suitability.

---

## Prompt 22: Poem Generation

**Domain:** Creative  
**Prompt Type:** Few-shot  
**Use Case:** Creative writing with constraints.

### Bad Prompt

```text
Write poem.
```

### Optimized Prompt

```text
Write a motivational poem for students. Style requirements: simple words, 4 stanzas, 4 lines per stanza, hopeful tone, no complex vocabulary. Theme: learning from failure.
```

### Why This Is Better

Adds format, tone, audience, and theme.

---

## Prompt 23: Brand Name Ideas

**Domain:** Creative  
**Prompt Type:** Reasoning summary  
**Use Case:** Naming a product or project.

### Bad Prompt

```text
Suggest names.
```

### Optimized Prompt

```text
Generate 15 brand name ideas for an AI learning app. For each name, include a one-line meaning and why it fits the product. Keep names short, memorable, and easy to pronounce.
```

### Why This Is Better

Adds quantity, evaluation criteria, and explanation.

---

## Prompt 24: YouTube Script

**Domain:** Creative  
**Prompt Type:** Zero-shot  
**Use Case:** Short-form educational content.

### Bad Prompt

```text
Make video script.
```

### Optimized Prompt

```text
Write a 60-second YouTube Shorts script explaining prompt engineering. Include hook, simple explanation, example, benefit, and call to action. Use a friendly student tone.
```

### Why This Is Better

Defines platform, duration, structure, and tone.

---

## Prompt 25: Ad Copy

**Domain:** Creative  
**Prompt Type:** Few-shot  
**Use Case:** Marketing copy generation.

### Bad Prompt

```text
Write ad.
```

### Optimized Prompt

```text
Create 5 advertisement captions for an AI note-taking app. Each caption should be under 15 words, include a clear benefit, and sound modern and student-friendly.
```

### Why This Is Better

Adds count, length limit, benefit focus, and audience.

---

# Reusable Prompt Template Library

## 1. General Task Template

```text
Act as a [role]. Your task is to [specific task].
Context: [background information].
Requirements:
- [requirement 1]
- [requirement 2]
- [requirement 3]
Output format: [table/bullets/paragraph/code].
Tone: [formal/friendly/academic/simple].
Constraints: [word limit/style/tools].
```

## 2. Coding Prompt Template

```text
Act as a [programming language] expert.
Task: [debug/explain/optimize/write] the following code.
Requirements:
- Explain the issue briefly.
- Provide corrected or improved code.
- Mention best practices.
Code:
[paste code here]
```

## 3. Writing Prompt Template

```text
Write a [content type] about [topic].
Audience: [target audience].
Tone: [tone].
Length: [word count].
Must include:
- [point 1]
- [point 2]
- [point 3]
Avoid: [things to avoid].
```

## 4. Summarization Prompt Template

```text
Summarize the following text for [audience].
Format:
- 5 bullet points
- 2-sentence summary
- 3 keywords
Rules:
- Keep the original meaning.
- Do not add new information.
Text:
[paste text here]
```

## 5. Analysis Prompt Template

```text
Analyze [topic/data/problem] using [framework].
Include:
- Key observations
- Evidence
- Risks
- Recommendations
Output format: [table/numbered list/report].
```

## 6. Creative Prompt Template

```text
Create a [story/poem/script/idea list] about [topic].
Style: [style].
Audience: [audience].
Constraints:
- [length]
- [tone]
- [format]
Include: [required elements].
```

## Conclusion

Effective prompt engineering improves AI output by making instructions clear, specific, contextual, and structured. Strong prompts define the role, task, audience, constraints, output format, and evaluation criteria. This prompt library can be reused and adapted for coding, writing, summarization, analysis, and creative projects.
