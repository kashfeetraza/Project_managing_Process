# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Dataset
# (You can replace this with your own dataset file)
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha", "Usman"],
    "Age": [22, 25, 23, 24, 22],
    "Marks": [85, 90, 78, 88, 76]
}

df = pd.DataFrame(data)

# Step 2: Display Data
print("Dataset:\n", df)

# Step 3: Basic Information
print("\nInfo:")
print(df.info())

# Step 4: Statistical Summary
print("\nStatistics:")
print(df.describe())

# Step 5: Data Cleaning (Example)
# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Step 6: Data Analysis
average_marks = df["Marks"].mean()
max_marks = df["Marks"].max()

print("\nAverage Marks:", average_marks)
print("Highest Marks:", max_marks)

# Step 7: Data Visualization
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()