# =====================================
# Fake News Detection (NLP Project)
# =====================================

# 1. Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 2. Create Sample Dataset
data = {
    "text": [
        "Government announces new economic policy",
        "Scientists discover new planet in solar system",
        "Click here to win 1 million dollars now",
        "Breaking: celebrity caught in scandal",
        "New education reforms introduced",
        "You won't believe what happened next",
        "Stock market reaches all time high",
        "This miracle cure will change your life"
    ],
    "label": [
        "real",
        "real",
        "fake",
        "fake",
        "real",
        "fake",
        "real",
        "fake"
    ]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# 3. Features & Target
X = df["text"]
y = df["label"]

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 5. Convert Text to Numerical Data (CountVectorizer)
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 6. Train Model (Naive Bayes)
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 7. Predictions
y_pred = model.predict(X_test_vec)

# 8. Evaluation
print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 9. Test with Custom Input
sample_news = ["Breaking news: government launches new scheme"]
sample_vec = vectorizer.transform(sample_news)

prediction = model.predict(sample_vec)
print("\nSample Prediction:", prediction[0])