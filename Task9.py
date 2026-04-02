# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    "Age": [22, 25, 47, 52, 46, 56, 23, 24, 45, 48],
    "Salary": [25000, 30000, 80000, 90000, 75000, 95000, 27000, 29000, 70000, 85000],
    "Experience": [1, 3, 15, 20, 12, 25, 2, 2, 10, 18]
}

df = pd.DataFrame(data)

# Step 2: Basic overview
print("First 5 rows:\n", df.head())

# Step 3: Correlation analysis
correlation = df.corr()
print("\nCorrelation:\n", correlation)

# Step 4: Visualization - Scatter Plot
plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.show()

# Step 5: Histogram (Distribution)
plt.hist(df["Age"])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Step 6: Insights
print("\nInsight:")
print("Salary increases with experience (positive correlation).")