# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 2. Load dataset
# Download from: https://grouplens.org/datasets/movielens/
ratings = pd.read_csv('ratings.csv')   # userId, movieId, rating
movies = pd.read_csv('movies.csv')     # movieId, title

# 3. Merge datasets
data = pd.merge(ratings, movies, on='movieId')

# 4. Create User-Item Matrix
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN with 0 (no rating)
user_movie_matrix_filled = user_movie_matrix.fillna(0)

# 5. Compute similarity between users
user_similarity = cosine_similarity(user_movie_matrix_filled)
user_similarity_df = pd.DataFrame(user_similarity,
                                 index=user_movie_matrix.index,
                                 columns=user_movie_matrix.index)

# 6. Function to get similar users
def get_similar_users(user_id, top_n=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # remove self
    return similar_users.head(top_n)

# 7. Recommendation function
def recommend_movies(user_id, num_recommendations=5):
    similar_users = get_similar_users(user_id)
    
    # Weighted ratings from similar users
    similar_users_ratings = user_movie_matrix.loc[similar_users.index]
    
    # Compute weighted average
    weighted_scores = similar_users_ratings.T.dot(similar_users)
    similarity_sum = similar_users.sum()
    
    recommendation_scores = weighted_scores / similarity_sum
    
    # Remove movies already watched
    watched_movies = user_movie_matrix.loc[user_id].dropna().index
    recommendation_scores = recommendation_scores.drop(watched_movies, errors='ignore')
    
    # Return top recommendations
    return recommendation_scores.sort_values(ascending=False).head(num_recommendations)

# 8. Example usage
user_id = 1
print("Top recommendations for User", user_id)
print(recommend_movies(user_id))