# Import libraries
import pandas as pd
import numpy as np

# Step 1: Create messy dataset
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", None],
    "Age": [22, np.nan, 23, 120, 21],
    "Salary": [50000, 60000, None, 70000, 65000]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Step 2: Handle Missing Values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Step 3: Fix Outliers (Age > 100 is unrealistic)
df.loc[df["Age"] > 100, "Age"] = df["Age"].mean()

# Step 4: Convert Data Types (if needed)
df["Age"] = df["Age"].astype(int)

# Step 5: Remove Duplicates (if any)
df.drop_duplicates(inplace=True)

print("\nCleaned Data:\n", df)

# Step 6: Basic Analysis
print("\nAverage Salary:", df["Salary"].mean())
print("Minimum Age:", df["Age"].min())
print("Maximum Age:", df["Age"].max())