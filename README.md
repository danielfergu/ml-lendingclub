# ML Algorithm to Predict Loan Repayment - LendingClub Data

## Introduction

The financial industry relies heavily on accurate risk assessment, especially in managing loan defaults. This project aims to develop a machine learning algorithm to predict loan repayment outcomes using LendingClub data. Accurate predictions can help financial institutions manage risk more effectively and make well-informed lending decisions.

## Project Goals

The primary objective of this project is to predict whether a loan will default based on borrower details and loan attributes. The focus is on reducing lender risk by accurately identifying potential defaults and approving reliable applicants.

## Dataset

The dataset is sourced from Lending Club and is publicly available on Kaggle. It includes detailed information about loans issued by Lending Club. For this project, a subset of 1.1 million rows and 151 columns is used.

Source:
George, N. (2018). All Lending Club loan data (Version 3.0) [Data set]. Kaggle. https://www.kaggle.com/datasets/wordsforthewise/lending-club

## Methodology

- Data Cleaning: Address missing values and inconsistencies.
- Exploratory Data Analysis (EDA): Uncover patterns and inform feature selection.
- Model Evaluation: Compare and select the best-performing model based on accuracy and robustness.

## Conclusion

Predicting loan defaults can significantly reduce lender risk. Key factors influencing loan repayment prediction include collection data, credit scores, socioeconomic variables, interest rates, and grading. Future improvements could involve feature refinement and enhanced data handling techniques.

## How to Run

Clone the repository.
Ensure you have the necessary dependencies installed.
Open the Jupyter notebook and run the cells to reproduce the analysis and results.

## Files

- **Notebook.ipynb**: Jupyter Notebook with the full analysis and code.
- **dataset/reducer.py**: Script to reduce the Kaggle dataset by half for easier use in a Jupyter Notebook.
- **dataset/download_reduced.py**: Script to directly download the reduced dataset.

## Feedback

Feel free to explore the notebook and provide feedback. Contributions are welcome!
