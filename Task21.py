# =====================================
# Stock Price Analysis (Time Series)
# =====================================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load Dataset (CSV)
# Example CSV format:
# Date,Open,High,Low,Close,Volume

df = pd.read_csv("stock_data.csv")

# 3. Data Preprocessing
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values("Date", inplace=True)

print("Dataset:\n", df.head())

# 4. Set Date as Index (important for time series)
df.set_index("Date", inplace=True)

# 5. Calculate Moving Averages
df["MA_5"] = df["Close"].rolling(window=5).mean()
df["MA_10"] = df["Close"].rolling(window=10).mean()

print("\nWith Moving Averages:\n", df.tail())

# 6. Plot Stock Price + Moving Averages
plt.figure(figsize=(10,5))

plt.plot(df["Close"], label="Closing Price")
plt.plot(df["MA_5"], label="5-Day Moving Avg")
plt.plot(df["MA_10"], label="10-Day Moving Avg")

plt.title("Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.show()

# 7. Basic Insights
print("\nBasic Insights:")
print("Average Closing Price:", df["Close"].mean())
print("Highest Price:", df["Close"].max())
print("Lowest Price:", df["Close"].min())