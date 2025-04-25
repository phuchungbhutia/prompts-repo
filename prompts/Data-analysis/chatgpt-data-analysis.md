--- 
title: Example Prompts for Data Analysis with ChatGPT 
category: Data-Analysis 
description: This document presents example prompts for utilizing ChatGPT to analyze research data effectively. Each prompt is tailored to specific data-related tasks, ensuring thorough and structured analysis. 
--- 

## 🔧 Prompt

1. **Clean and Structure Your Data**
   - **Prompt:**  
     > "I have a dataset with inconsistent date formats, duplicate entries, and some typos in column names. Can you help me clean and standardize it for analysis?"
   - **Purpose:**  
     Organize the dataset for improved reliability and accuracy in analysis.

2. **Explore and Summarize Insights**
   - **Prompt:**  
     > "Here's a dataset of customer survey results. Can you highlight key trends, patterns, and averages, and explain what they suggest in simple terms?"
   - **Purpose:**  
     Extract meaningful insights and identify patterns within the data.

3. **Create Visualizations**
   - **Prompt:**  
     > "Can you create a bar chart showing the number of sales per region and a pie chart showing the distribution of product categories from this dataset?"
   - **Purpose:**  
     Represent data visually for better comprehension and decision-making.

4. **Run Statistical Analysis**
   - **Prompt:**  
     > "Can you perform a t-test to compare the average scores of two groups in this study? Also, explain the results in plain language."
   - **Purpose:**  
     Validate hypotheses and interpret results using statistical methods.

5. **Work with Interactive Tables**
   - **Prompt:**  
     > "Help me turn this static dataset into an interactive table where I can filter by date and sort by total sales amount."
   - **Purpose:**  
     Enable dynamic data exploration for deeper insights.

6. **Generate Reports**
   - **Prompt:**  
     > "Can you generate a summary report based on this dataset? Include key findings, charts, and a structured breakdown of results."
   - **Purpose:**  
     Produce comprehensive reports for documentation and presentation.

--- 

## 🧩 Inputs

- `dataset`: The dataset to be cleaned, analyzed, or visualized (e.g., CSV, Excel file).
- `statistical_tests`: The type of statistical analysis to perform (e.g., t-test, chi-square).
- `visualization_types`: Types of visualizations to create (e.g., bar chart, pie chart).
- `report_structure`: Desired structure for the report (e.g., key findings, charts, conclusion).

---

## ⚙️ Constraints

- Ensure the data is cleaned and standardized before analysis.
- Use clear and simple language for explaining insights and statistical results.
- Visualizations should be concise, easy to interpret, and relevant to the dataset.
- Reports must include key findings, visual elements, and a structured analysis.

---

## 📋 Output Format

```markdown
# Data Analysis Report

## Data Cleaning and Structuring
- The dataset has been cleaned and standardized, removing duplicate entries and fixing inconsistencies in column names and date formats.

## Key Insights and Patterns
- **Trend 1:** [Describe the first key trend identified.]
- **Pattern 1:** [Describe the pattern or insight drawn from the data.]

## Visualizations
- **Bar Chart:** Number of sales per region.
- **Pie Chart:** Distribution of product categories.

## Statistical Analysis
- **Test Performed:** [Describe the statistical test performed, e.g., t-test.]
- **Results:** [Describe the result and interpretation.]

## Interactive Table
- The data has been transformed into an interactive table for filtering and sorting by various parameters (e.g., date, total sales).

## Summary Report
- The report includes key findings, visualizations, and a structured breakdown of results, providing a clear overview of the dataset.
