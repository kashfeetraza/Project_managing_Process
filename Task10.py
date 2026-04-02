# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Create dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [50, 55, 60, 65, 70, 75, 80, 90],
    "Pass": [0, 0, 0, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

# Step 2: Features and target
X = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Predictions
y_pred = model.predict(X_test)

# Step 6: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Step 7: Predict new student
new_data = [[5, 70]]  # 5 hours, 70% attendance
prediction = model.predict(new_data)

print("Prediction (0=Fail, 1=Pass):", prediction[0])