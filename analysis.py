import pandas as pd
import numpy as np

# Load a public dataset (example: Titanic)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Print first few rows
print("First few rows of data:")
print(data.head())

# Check column data types
print("\nData Types:")
print(data.info())

# Summary statistics
# print("\nSummary Statistics:")
# print(data.describe())

# Calculate basic statistics
mean_values = data.mean(numeric_only=True)
median_values = data.median(numeric_only=True)
mode_values = data.mode().iloc[0]  # First mode row
std_dev_values = data.std(numeric_only=True)

print("\nMean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nMode:\n", mode_values)
print("\nStandard Deviation:\n", std_dev_values)

# Calculate correlation
print("\nFeature Correlations:")
print(data.corr(numeric_only=True))
