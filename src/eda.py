
# SWYNEX INTERNSHIP - TASK 2
# Exploratory Data Analysis (EDA)
# Dataset: Netflix Movies and TV Shows

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n========== DATASET OVERVIEW ==========")

# Display first five records
print("\nFirst 5 Rows:")
print(df.head())

# Dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Column information
print("\nColumn Names:")
print(df.columns.tolist())

# Data types and non-null counts
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\n========== DATASET OVERVIEW ==========")

# Display first five records
print("\nFirst 5 Rows:")
print(df.head())

# Dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Column information
print("\nColumn Names:")
print(df.columns.tolist())

# Data types and non-null counts
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
