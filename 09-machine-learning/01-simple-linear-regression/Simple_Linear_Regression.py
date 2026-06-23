# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# ============================================================
# SIMPLE LINEAR REGRESSION — FULL 7-PHASE INDUSTRY PIPELINE
# Problem: Predict Salary based on Years of Experience
# ============================================================
 
# ============================================================
# PHASE 1: BUSINESS & DATA UNDERSTANDING (Steps 1-5)
# ============================================================
 
# Step 1 (Business problem) — no code, just understanding:
# "Estimate appropriate salary offers based on years of experience"
 
# Step 3 — Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Step 3 — Load dataset (change path to your file location)
dataset = pd.read_csv("Salary_Data.csv")

# Step 4 — Understand columns
print(dataset.columns)
print(dataset.head)
# Step 5 — Check structure
print(dataset.shape)
print(dataset.dtypes)

# ============================================================
# PHASE 2: EXPLORATORY DATA ANALYSIS (Steps 6-11)
# ============================================================
 # Step 6 — Missing values
print("Missing values:\n",dataset.isnull().sum())

# Step 7 — Duplicates
print("Duplicate rows:", dataset.duplicated().sum())
 

# Step 8 — Univariate stats (descriptive statistics)
print(dataset.describe())
print("Skewness:\n", dataset.skew())


# Step 9 — Bivariate analysis (correlation between feature and target)
correlation = dataset['YearsExperience'].corr(dataset['Salary'])
print(f"Correlation between Experience and Salary: {correlation:.3f}")
 
# Step 10 — Visualize distribution
plt.hist(dataset['Salary'], bins=10, color='skyblue', edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Step 11 — Visualize relationship (raw scatter before modeling)
plt.scatter(dataset['YearsExperience'], dataset['Salary'], color='red')
plt.title('Years of Experience vs Salary — Raw Data')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


 
# ============================================================
# PHASE 3: DATA CLEANING & FEATURE ENGINEERING (Steps 12-18)
# ============================================================
 
# Step 12-14 — Handle missing values / outliers / duplicates
# (Checked in Phase 2 — this dataset is already clean.
#  If issues existed, you would handle them HERE before proceeding.)
 
# Step 15-18 — Encoding / Feature engineering / Multicollinearity
# Not applicable — only ONE independent variable (YearsExperience).
# This is exactly why it's called SIMPLE Linear Regression.

# ============================================================
# PHASE 4: DATA PREPARATION FOR MODELING (Steps 19-22)
# ============================================================
 
# Step 19 — Split into X (independent variable) and y (dependent variable)
x = dataset.iloc[:, :-1]    # YearsExperience
y = dataset.iloc[:, -1]     # Salary

# Step 20 — Train-test split (80-20)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)


# Step 21 — Feature scaling
# Not required here — only one feature, nothing to balance against.
 
# Step 22 — Class imbalance
# Not applicable — this is regression, not classification.
 
 
# ============================================================
# PHASE 5: MODEL BUILDING & TRAINING (Steps 23-26)
# ============================================================
 
# Step 23 — Choose baseline model


from sklearn.linear_model import LinearRegression
 
regressor = LinearRegression()


# Step 24 — Train (fit) the model
regressor.fit(x_train,y_train)

# Step 25 — Predict on test set
y_pred = regressor.predict(x_test)
# Step 26 — Evaluate on BOTH train and test (bias vs variance check)
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
 
train_pred = regressor.predict(x_train)
train_r2 = r2_score(y_train,train_pred)
test_r2 = r2_score(y_test,y_pred)

mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

 
print(f"Training R² (bias check):  {train_r2:.4f}")
print(f"Test R² (variance check):  {test_r2:.4f}")
print(f"MAE:  £{mae:,.2f}")
print(f"MSE:  £{mse:,.2f}")
print(f"RMSE: £{rmse:,.2f}")


# Inspect the learned equation: y = mx + c
m = regressor.coef_[0]        # slope (beta_1)
c = regressor.intercept_      # intercept (beta_0)

 
print(f"\nLearned Equation: Salary = {m:.2f} * YearsExperience + {c:.2f}")

x_value = 12
y_manual = m * x_value + c
print(f"Manual calculation: £{y_manual:,.2f}")

# ============================================================
# PHASE 6: MODEL VALIDATION & IMPROVEMENT (Steps 27-30)
# ============================================================
 
# Step 27 — Cross-validation (confirm result isn't a lucky split)
from sklearn.model_selection import cross_val_score
 
cv_scores = cross_val_score(regressor, x, y, cv=5)
print(f"\nCross-validation R² scores: {cv_scores}")
print(f"Average CV R²: {cv_scores.mean():.4f}")
print(f"Std dev across folds: {cv_scores.std():.4f}")
 

 
# Step 28 — Hyperparameter tuning
# Not applicable — Simple Linear Regression has no hyperparameters to tune.
 
# Step 29 — Compare multiple models
# Not applicable at SLR stage — becomes relevant from MLR/Polynomial onward.
 
# Step 30 — Final evaluation + visualization
 
# Visualize training set fit
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
 
# Visualize test set fit
plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Forecast genuinely new/unseen cases
years_12 = 12
salary_12_pred = regressor.predict([[years_12]])
print(f"\nPredicted salary at {years_12} years experience: £{salary_12_pred[0]:,.2f}")
 
years_20 = 20
salary_20_pred = regressor.predict([[years_20]])
print(f"Predicted salary at {years_20} years experience: £{salary_20_pred[0]:,.2f}")
 
 
# Step 31 — Pickle (save) the trained model
import pickle
 
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file) 
 
print(f"\nModel has been pickled and saved as {filename}")
