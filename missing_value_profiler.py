# missing_value_profiler.py

"""
Missing Value Profiler
----------------------
This script performs deep analysis of missing data in a DataFrame:
- Percentage of missing values per column
- Pattern detection of null combinations
- Row-wise missing count distribution
- Column clustering based on missing patterns
- Heatmap and barplot visualizations
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations

# Generate synthetic dataset with structured missingness
np.random.seed(0)
n = 1000
data = {
    'age': np.random.randint(18, 80, n).astype(float),
    'income': np.random.normal(50000, 10000, n),
    'gender': np.random.choice(['M', 'F'], n),
    'married': np.random.choice([True, False], n),
    'children': np.random.poisson(2, n).astype(float),
    'zipcode': np.random.choice(['1000', '2000', '3000'], n)
}

# Introduce missing patterns
df = pd.DataFrame(data)
df.loc[df['income'] < 45000, 'age'] = np.nan
df.loc[df['children'] == 0, 'married'] = np.nan
df.loc[np.random.rand(n) < 0.1, 'income'] = np.nan
df.loc[np.random.rand(n) < 0.05, 'children'] = np.nan

# Basic missing value stats
print("\nMISSING VALUE PERCENTAGES:")
missing_percent = df.isnull().mean().sort_values(ascending=False) * 100
print(missing_percent)

# Row-wise missing count distribution
row_missing = df.isnull().sum(axis=1)
plt.figure(figsize=(8, 4))
sns.histplot(row_missing, bins=range(0, df.shape[1]+1), discrete=True, color='purple')
plt.title("Distribution of Missing Values per Row")
plt.xlabel("Number of Missing Values")
plt.tight_layout()
plt.show()

# Heatmap of nulls
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="Reds")
plt.title("Missing Value Heatmap")
plt.tight_layout()
plt.show()

# Detect most frequent null patterns
null_pattern_counts = df.isnull().astype(int).apply(lambda row: tuple(row), axis=1)
pattern_summary = null_pattern_counts.value_counts().head(5)
print("\nTOP 5 MISSING VALUE PATTERNS (as binary vectors):")
print(pattern_summary)

# Co-occurrence heatmap
co_occur = pd.DataFrame(0, index=df.columns, columns=df.columns)
for col1, col2 in combinations(df.columns, 2):
    both_null = df[col1].isnull() & df[col2].isnull()
    co_occur.loc[col1, col2] = both_null.sum()
    co_occur.loc[col2, col1] = both_null.sum()

plt.figure(figsize=(8, 6))
sns.heatmap(co_occur, annot=True, fmt='d', cmap='YlOrBr')
plt.title("Null Co-occurrence Between Columns")
plt.tight_layout()
plt.show()

# Final insight
print("\nINSIGHTS:")
print("- Columns with >30% missing might require imputation/exclusion.")
print("- Strong null co-occurrence suggests dependency in missing mechanisms.")
print("- Frequent patterns may help in building imputation strategies or segmenting data.")
