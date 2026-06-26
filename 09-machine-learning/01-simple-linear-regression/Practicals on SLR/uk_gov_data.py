# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# =====================================================================
# SIMPLE LINEAR REGRESSION — PRACTICAL 2 (data.gov.uk: EPC open data)
# Full 7-Phase / 32-Step Master Pipeline
# Source: https://epc.opendatacommunities.org/  (filter to ONE local
#         authority, e.g. LB Sutton, download zip -> certificates.csv)
# IV (X): TOTAL_FLOOR_AREA (m2)      |   Target (y): CO2_EMISSIONS_CURRENT (tonnes/yr)
# Run phase by phase in Spyder using the  # %%  cell markers.
# NOTE: run Phases 1-2 FIRST and report output back before trusting Phase 3.
# =====================================================================
 
# ---- Config (change target here if you want heating cost instead) ----
IV_COL     = 'TOTAL_FLOOR_AREA'
TARGET_COL = 'CO2_EMISSIONS_CURRENT'      # alt: 'HEATING_COST_CURRENT' (GBP/yr)
TARGET_UNIT = 'tonnes/yr'                 # alt: 'GBP' if using heating cost
CSV_PATH   = 'certificates.csv'
 
 
# %% PHASE 1: BUSINESS & DATA UNDERSTANDING ===========================
 
# Step 1 — Business Problem:
#   A local authority housing/net-zero team wants to estimate a dwelling's
#   annual CO2 emissions from its floor area, to prioritise retrofit and
#   insulation schemes across the borough's housing stock.
 
# Step 2 — Target Variable & Success Metric:
#   Target (y) = CO2_EMISSIONS_CURRENT (continuous -> regression).
#   Success = predictions within an acceptable error margin (R^2 and RMSE).
 
# Step 3 — Acquire Dataset:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# Real EPC file is wide (~90 cols) and mixed-type -> low_memory=False
dataset_full = pd.read_csv(CSV_PATH, low_memory=False)
 
# Step 4 — Understand Columns:
#   The file has ~90 columns. For SLR we use exactly TWO:
#     TOTAL_FLOOR_AREA       -> IV  (X) -> dwelling size in m2
#     CO2_EMISSIONS_CURRENT  -> DV  (y) -> annual CO2 emissions in tonnes/yr
 
# Step 5 — Check Structure:
print("Full file shape:", dataset_full.shape)          # e.g. (~80000, ~90)
print("Total columns:", len(dataset_full.columns))
print(dataset_full[[IV_COL, TARGET_COL]].dtypes)       # often 'object' -> needs coercion
print(dataset_full[[IV_COL, TARGET_COL]].head())
 
 
# %% PHASE 2: EXPLORATORY DATA ANALYSIS ===============================
# (Run on the RAW two columns so you see the mess before cleaning.)
 
raw = dataset_full[[IV_COL, TARGET_COL]].copy()
 
# Step 6-7 — Missing Values & Duplicates:
print("Missing values:\n", raw.isnull().sum())
print("Fully-duplicated rows:", raw.duplicated().sum())
 
# Step 8 — Univariate Stats (coerce to numeric just for inspection):
raw_num = raw.apply(pd.to_numeric, errors='coerce')
print(raw_num.describe())
print("Skewness:\n", raw_num.skew())
# Watch for: impossible mins (0 or negative), absurd maxes (e.g. 9999 m2).
 
# Step 9 — Bivariate Analysis (feature vs target):
correlation = raw_num[IV_COL].corr(raw_num[TARGET_COL])
print(f"Correlation: {correlation:.3f}")
# Expect a clear POSITIVE correlation -> supports SLR.
 
# Step 10-11 — Visualise (sample for a readable scatter on big data):
sample = raw_num.dropna().sample(min(2000, len(raw_num.dropna())), random_state=0)
plt.scatter(sample[IV_COL], sample[TARGET_COL], s=6, alpha=0.3, color='red')
plt.title('Floor Area vs CO2 Emissions - Raw Sample')
plt.xlabel('Total Floor Area (m2)')
plt.ylabel(f'CO2 Emissions ({TARGET_UNIT})')
plt.show()
# >>> STOP HERE on first run. Report Steps 5-9 output back before Phase 3. <<<
 
 
# %% PHASE 3: DATA CLEANING & FEATURE ENGINEERING =====================
# This is where Practical 2 earns its keep - real cleaning, each step stated.
 
df = dataset_full[[IV_COL, TARGET_COL]].copy()
 
# Step 12 — Coerce to numeric (text/blank entries become NaN):
df[IV_COL]     = pd.to_numeric(df[IV_COL], errors='coerce')
df[TARGET_COL] = pd.to_numeric(df[TARGET_COL], errors='coerce')
 
# Step 13 — Drop missing rows in either column:
before = len(df)
df = df.dropna(subset=[IV_COL, TARGET_COL])
print(f"Dropped {before - len(df)} rows with missing IV/target.")
 
# Step 14 — Remove impossible values / gross outliers (adjust after seeing EDA):
#   Floor area: keep sensible dwelling range; CO2: must be > 0.
before = len(df)
df = df[(df[IV_COL] > 10) & (df[IV_COL] < 1000)]
df = df[df[TARGET_COL] > 0]
print(f"Dropped {before - len(df)} implausible/outlier rows.")
 
# Also drop exact duplicate (area, co2) rows:
before = len(df)
df = df.drop_duplicates()
print(f"Dropped {before - len(df)} duplicate rows. Final shape: {df.shape}")
 
# Step 15-18 — Encoding / Feature Engineering / Multicollinearity:
#   NOT APPLICABLE, and here's why (stated explicitly per the rule):
#     - We deliberately selected ONE numeric IV (TOTAL_FLOOR_AREA) to keep
#       this SIMPLE Linear Regression -> no categorical columns to encode.
#     - No derived features needed for a single predictor.
#     - Multicollinearity needs 2+ features to exist.
 
 
# %% PHASE 4: DATA PREPARATION FOR MODELING ===========================
 
# Step 19 — Split X and y:
X = df.iloc[:, :-1].values    # TOTAL_FLOOR_AREA
y = df.iloc[:, -1].values     # CO2_EMISSIONS_CURRENT
 
# STRUCTURE GUARD (makes "confirm structure" mechanical):
assert X.shape[1] == 1, f"SLR requires exactly 1 feature, but X has {X.shape[1]}."
print(f"Structure OK -> X has {X.shape[1]} feature, {X.shape[0]} rows.")
 
# Step 20 — Train-Test Split:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0
)
 
# Step 21 — Feature Scaling:
#   NOT required for SLR with one feature - nothing to balance against.
 
# Step 22 — Class Imbalance:
#   NOT APPLICABLE - this is regression, not classification.
 
 
# %% PHASE 5: MODEL BUILDING & TRAINING ===============================
 
# Step 23 — Choose Baseline Model:
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
 
# Step 24 — Train (fit):
regressor.fit(X_train, y_train)
 
# Step 25 — Predict:
y_pred = regressor.predict(X_test)
 
# Step 26 — Evaluate on BOTH Train and Test:
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
train_r2 = r2_score(y_train, regressor.predict(X_train))   # BIAS
test_r2  = r2_score(y_test, y_pred)                         # VARIANCE
print(f"Training R2 (bias):    {train_r2:.4f}")
print(f"Test R2 (variance):    {test_r2:.4f}")
 
mae  = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE:  {mae:,.3f} {TARGET_UNIT}")
print(f"RMSE: {rmse:,.3f} {TARGET_UNIT}")
 
# Learned equation:
m = regressor.coef_[0]
c = regressor.intercept_
print(f"Equation: CO2 = {m:.4f} x FloorArea + {c:.4f}")
 
 
# %% PHASE 6: MODEL VALIDATION & IMPROVEMENT ==========================
 
# Step 27 — Cross-Validation:
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(regressor, X, y, cv=5)
print(f"CV scores: {cv_scores}")
print(f"Average CV R2: {cv_scores.mean():.4f}")
print(f"Std dev across folds: {cv_scores.std():.4f}")
 
# Step 28 — Hyperparameter Tuning:
#   SLR has essentially no hyperparameters (relevant later: Ridge/Lasso/RF).
 
# Step 29 — Compare Models:
#   Not meaningful with one SLR model family; becomes critical from MLR onward.
 
# Step 30 — Final Evaluation:
print(f"FINAL TEST R2: {test_r2:.4f}")
print(f"FINAL RMSE:    {rmse:,.3f} {TARGET_UNIT}")
 
# Visualise the fit (sample test points for readability):
idx = np.random.RandomState(0).choice(len(X_test), size=min(2000, len(X_test)), replace=False)
plt.scatter(X_test[idx], y_test[idx], s=6, alpha=0.3, color='red')
plt.plot(X_test, regressor.predict(X_test), color='blue', linewidth=2)
plt.title('Floor Area vs CO2 (Test Set + Fitted Line)')
plt.xlabel('Total Floor Area (m2)')
plt.ylabel(f'CO2 Emissions ({TARGET_UNIT})')
plt.show()
 
# Forecast new dwellings:
for area in (75, 150):
    pred = regressor.predict([[area]])
    print(f"Predicted CO2 at {area} m2: {pred[0]:,.3f} {TARGET_UNIT}")
 
 
# %% PHASE 7: DEPLOYMENT & OPERATIONS =================================
 
# Step 31 — Pickle the Model:
import pickle
filename = 'epc_slr_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print(f"Model saved as {filename}")
 
# Step 32 — Deployment Plan:
#   Front end : Flask/FastAPI form -> user enters floor area (m2)
#   Backend   : Loads pickled model -> regressor.predict()
#   Hosting   : AWS / Azure / Google Cloud
#   CI/CD     : Auto-redeploy when retrained on new EPC releases (monthly)
#   MLOps     : Monitor drift - EPC data updates monthly; retrain if the
#               area->CO2 relationship shifts (e.g. after retrofit schemes).