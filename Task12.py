# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load dataset
# Download from Kaggle: https://www.kaggle.com/c/titanic/data
data = pd.read_csv('train.csv')  # path to train.csv

# 3. Basic EDA
print(data.head())
print(data.info())
print(data.describe())
print(data['Survived'].value_counts())

# 4. Data Cleaning
# Fill missing Age values with median
data['Age'].fillna(data['Age'].median(), inplace=True)

# Fill missing Embarked values with mode
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Drop columns not useful for prediction
data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)

# 5. Encode categorical features
le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
data['Embarked'] = le.fit_transform(data['Embarked'])

# 6. Feature-target split
X = data.drop('Survived', axis=1)
y = data['Survived']

# 7. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 9. Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 10. Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))