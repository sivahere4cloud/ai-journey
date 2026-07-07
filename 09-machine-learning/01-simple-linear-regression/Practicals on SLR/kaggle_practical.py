# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:59:56 2026

@author: sivag
"""
#Phase :: 1

# Step 3 — Acquire Dataset:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#load and read the dataset
dataset = pd.read_csv(r"C:\Users\sivag\git-projects\ai-journey\09-machine-learning\01-simple-linear-regression\Practicals on SLR\Salary_dataset.csv")

dataset.head()
# Step 4 — Understand Columns:
#   YearsExperience -> IV  (X) -> how long someone has worked
#   Salary          -> DV  (y) -> what they currently earn


dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]
# Step 5 — Check Structure:
print(dataset.shape)          # expect (30, 2)
print(dataset.dtypes)         # both float64
print(dataset.head())

# %% PHASE 2: EXPLORATORY DATA ANALYSIS ===============================

 
# Step 6-7 — Missing Values & Duplicates:
print("Missing values:\n", dataset.isnull().sum())
print("Duplicate rows:", dataset.duplicated().sum())
print("Missing values:\n", dataset.isnull().sum())
print("Duplicate rows:", dataset.duplicated().sum())

# Step 8 — Univariate Stats:
print(dataset.describe())
print("Skewness : \n",dataset.skew())

# Step 9 — Bivariate Analysis (feature vs target):
correlation = dataset['YearsExperience'].corr(dataset['Salary'])
print(f"Correlation: {correlation:.3f}")   

# Expect a STRONG positive correlation -> that's WHY this is a good SLR candidate.

# Step 10-11 — Visualise raw data:
    
plt.scatter(dataset['YearsExperience'],dataset['Salary'],color='r')
plt.title('Years of Experience vs Salary - Raw Data')
plt.xlabel('Years of Exp')
plt.ylabel('Salary')
plt.show()

 

# %% PHASE 4: DATA PREPARATION FOR MODELING ===========================
 
# Step 19 — Split X and y:
X = dataset.iloc[:, :-1].values    
y = dataset.iloc[:, -1].values   
 
# STRUCTURE GUARD (makes the "confirm structure" rule mechanical):
assert X.shape[1] == 1, f"SLR requires exactly 1 feature, but X has {X.shape[1]}. Check the CSV columns."
print(f"Structure OK -> X has {X.shape[1]} feature, {X.shape[0]} rows.")
 
 
# Step 20 — Train-Test Split:
from sklearn.model_selection import train_test_split
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)
 

 
# %% PHASE 5: MODEL BUILDING & TRAINING ===============================
 
# Step 23 — Choose Baseline Model:
from sklearn.linear_model import LinearRegression
 
regressor = LinearRegression()
 
# Step 24 — Train (fit):
regressor.fit(X_train, y_train)
# scikit-learn now solves for m (slope) and c (intercept) by minimising
# squared error across the training points.
 
# Step 25 — Predict:
y_pred = regressor.predict(X_test)
 
# Step 26 — Evaluate on BOTH Train and Test:
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
 
train_pred = regressor.predict(X_train)
train_r2 = r2_score(y_train, train_pred)     # BIAS check
test_r2 = r2_score(y_test, y_pred)           # VARIANCE check
 
print(f"Training R2 (bias):    {train_r2:.4f}")
print(f"Test R2 (variance):    {test_r2:.4f}")
 
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE:  GBP {mae:,.2f}")
print(f"RMSE: GBP {rmse:,.2f}")
 
# Inspect the learned equation:
m = regressor.coef_[0]        # slope (beta_1)
c = regressor.intercept_      # intercept (beta_0)
print(f"Equation: Salary = {m:.2f} x YearsExperience + {c:.2f}")
 
 
# %% PHASE 6: MODEL VALIDATION & IMPROVEMENT ==========================
 
# Step 27 — Cross-Validation:
from sklearn.model_selection import cross_val_score
 
cv_scores = cross_val_score(regressor, X, y, cv=5)
print(f"CV scores: {cv_scores}")
print(f"Average CV R2: {cv_scores.mean():.4f}")
print(f"Std dev across folds: {cv_scores.std():.4f}")
# Low std dev = consistent performance = stable model, not overfitting.
 

 
# Step 30 — Final Evaluation:
print(f"FINAL TEST R2: {test_r2:.4f}")
print(f"FINAL RMSE:    GBP {rmse:,.2f}")
 
# Visualise the fit - training set:
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
 
# Visualise the fit - test set (same fitted line):
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
 
# Forecast genuinely new/future cases:
salary_12 = regressor.predict([[12]])
print(f"Predicted salary at 12 years: GBP {salary_12[0]:,.2f}")
 
salary_20 = regressor.predict([[20]])
print(f"Predicted salary at 20 years: GBP {salary_20[0]:,.2f}")
 
 
# %% PHASE 7: DEPLOYMENT & OPERATIONS =================================
 
# Step 31 — Pickle the Model:
import pickle
 
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print(f"Model saved as {filename}")
 
# Step 32 — Deployment Plan:
#   Front end : Flask/FastAPI form -> user enters years of experience
#   Backend   : Loads pickled model -> calls regressor.predict()
#   Hosting   : AWS / Azure / Google Cloud
#   CI/CD     : Auto-deploy when the model is retrained
#   MLOps     : Monitor drift - if real salaries drift from predictions, retrain.


































