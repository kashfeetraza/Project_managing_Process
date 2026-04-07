# ================================
# Student Performance Prediction
# ================================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 2. Create Dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "marks": [30, 35, 40, 50, 55, 60, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# 3. Define Features & Target
X = df[["study_hours", "attendance"]]
y = df["marks"]

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# 7. Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)

# 8. Model Insights
print("\nModel Details:")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 9. Visualization
plt.scatter(df["study_hours"], df["marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# 10. Predict New Data
new_data = pd.DataFrame({
    "study_hours": [6],
    "attendance": [80]
})

prediction = model.predict(new_data)
print("\nPredicted Marks for (6 hrs study, 80% attendance):", prediction[0])