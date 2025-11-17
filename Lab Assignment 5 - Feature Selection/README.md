# Feature Selection Lab - Loan Prediction Dataset (Ashwin Satish)

## Overview

This Jupyter notebook demonstrates various feature selection techniques applied to a loan prediction dataset. The goal is to identify the most relevant features for predicting whether a loan will be paid back.
Dataset
The lab uses a synthetic loan prediction dataset from Kaggle, which contains 20,000 records with 22 features including:

- Borrower demographics (age, gender, marital status, education)
- Financial information (income, credit score, debt-to-income ratio)
- Loan details (amount, term, interest rate, purpose)
- Credit history (delinquencies, open accounts, credit limit)

## Feature Selection Methods Implemented

1. Correlation Analysis

Examines relationships between features and the target variable
Identifies multicollinearity among features
Provides initial insights into feature relevance

2. Univariate Selection (F-test)

Uses statistical tests to select top 20 features
Based on ANOVA F-statistic for classification
Filters features based on their individual predictive power

3. Recursive Feature Elimination (RFE)

Iteratively removes least important features
Uses Random Forest as the base estimator
Selects top 20 features through backward elimination

4. Feature Importance (Random Forest)

Leverages tree-based model feature importance
Visualizes importance scores via bar chart
Selects 16 features with importance > 0.013

5. Mutual Information

Measures dependency between features and target
Captures both linear and non-linear relationships
Selects top 20 features based on MI scores

6. Boruta

All-relevant feature selection algorithm
Compares feature importance against random shadow features
Identifies 6 most statistically relevant features

## Model Performance Comparison

All feature selection methods are evaluated using a Random Forest classifier with the following metrics:

- Accuracy
- ROC AUC
- Precision
- Recall
- F1 Score

Results show that RFE achieved the highest performance (90% accuracy) with 20 features, while Boruta achieved competitive results (89.4% accuracy) with only 6 features, demonstrating the most efficient dimensionality reduction.

## Key Findings

Most Important Features: employment_status_Unemployed, debt_to_income_ratio, credit_score, grade_subgrade_encoded
Best Performance: RFE with 20 features (90% accuracy, 0.764 ROC AUC)
Most Efficient: Boruta with 6 features (89.4% accuracy, 0.766 ROC AUC)
