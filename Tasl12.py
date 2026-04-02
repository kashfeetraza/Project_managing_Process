import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    "title": [
        "The Matrix", "John Wick", "Avengers", 
        "Iron Man", "Batman", "Superman"
    ],
    "genre": [
        "sci-fi action", "action thriller", "superhero action",
        "superhero tech", "dark superhero", "superhero alien"
    ]
}

df = pd.DataFrame(data)

# Convert text data into vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["genre"])

# Compute similarity
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name):
    index = df[df["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations for {movie_name}:\n")
    for i in sorted_scores[1:4]:
        print(df.iloc[i[0]]["title"])

# Test
recommend("The Matrix")