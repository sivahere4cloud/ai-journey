# Simple Linear Regression — Salary Prediction

End-to-end implementation of a Simple Linear Regression model to predict salary from years of professional experience. Built following a 7-phase industry pipeline covering business understanding, data preparation, modeling, evaluation, and interpretation.

## 🎯 Problem Statement

Estimate appropriate salary offers based on a candidate's years of experience. Useful for HR teams setting competitive compensation, candidates benchmarking expected offers, and recruiters validating salary ranges.

## 📊 Dataset

**`Salary_Data.csv`** — 30 records with two columns:

| Column | Description |
|---|---|
| `YearsExperience` | Years of professional experience (continuous, 1.1–10.5) |
| `Salary` | Annual salary in USD (continuous) |

## 🛠️ Tech Stack

- **Python** — Core language
- **NumPy** — Numerical operations
- **Pandas** — Data loading and manipulation
- **Matplotlib** — Visualization
- **scikit-learn** — Linear Regression model and train-test split

## 🧭 7-Phase Pipeline Followed

1. **Business & Data Understanding** — Define problem, load data, inspect structure
2. **Data Preparation** — Feature/target split, train-test split
3. **Model Building** — Fit Simple Linear Regression
4. **Prediction** — Generate predictions on test set
5. **Evaluation** — R², MAE, MSE, RMSE metrics
6. **Visualization** — Regression line on train and test sets
7. **Interpretation** — Coefficient meaning and business takeaways

## 🚀 How to Run

```bash
pip install numpy pandas matplotlib scikit-learn

python Simple_Linear_Regression.py
```

## 📂 Files

- `Simple_Linear_Regression.py` — Main implementation
- `Salary_Data.csv` — Dataset
- `README.md` — This file

## 📝 Status

🔧 In progress — currently completing Phase 1 (Business & Data Understanding). Remaining phases will be added incrementally.