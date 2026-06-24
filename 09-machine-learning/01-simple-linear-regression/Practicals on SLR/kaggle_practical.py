# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:59:56 2026

@author: sivag
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\sivag\git-projects\ai-journey\09-machine-learning\01-simple-linear-regression\Practicals on SLR\Salary_dataset.csv")

dataset.head()

dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]
print(dataset.shape)          # expect (30, 2)
print(dataset.dtypes)         # both float64
print(dataset.head())

#EDA
print("Missing values:\n", dataset.isnull().sum())
print("Duplicate rows:", dataset.duplicated().sum())