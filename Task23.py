# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset (CSV file)
# Example: create a sample CSV-like dataset
data = {
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Laptop"],
    "Price": [80000, 30000, 75000, 40000, 32000, 82000],
    "Quantity": [2, 5, 1, 3, 4, 2]
}

df = pd.DataFrame(data)

# Step 2: Show dataset
print("Dataset:\n", df)

# Step 3: Create new column (Feature Engineering)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nWith Total Sales:\n", df)

# Step 4: Grouping (Important Data Science concept)
sales_summary = df.groupby("Product")["Total_Sales"].sum()

print("\nSales Summary:\n", sales_summary)

# Step 5: Find Best Selling Product
best_product = sales_summary.idxmax()
print("\nBest Selling Product:", best_product)

# Step 6: Visualization
sales_summary.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()