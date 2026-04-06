import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load your dataset
df = pd.read_csv('housing_data.csv')

# 2. Select Features (X) and Target (y)
# Let's assume 'SalePrice' is what we want to predict
X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'OverallQual']] 
y = df['SalePrice']

# 3. Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make Predictions
predictions = model.predict(X_test)

# 6. Evaluate
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print(f"RMSE: ${rmse:,.2f}")
print(f"R-squared Score: {r2:.2f}")