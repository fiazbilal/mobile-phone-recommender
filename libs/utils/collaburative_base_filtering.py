import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Example data: User-Item interactions (ratings or clicks)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
    'item_id': [101, 102, 103, 101, 104, 102, 105, 103],
    'rating': [5, 3, 4, 4, 5, 2, 3, 5]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a pivot table where rows are users and columns are items
pivot_table = df.pivot(index='user_id', columns='item_id', values='rating').fillna(0)

# Transpose the table (user-item matrix)
user_item_matrix = pivot_table.values

# Create a NearestNeighbors model
model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=2)

# Fit the model to the user-item matrix
model.fit(user_item_matrix)

# Make a prediction (find nearest neighbors for a given user)
user_id = 1  # User for whom we want recommendations
user_index = pivot_table.index.get_loc(user_id)

# Find 2 nearest neighbors (users)
distances, indices = model.kneighbors(user_item_matrix[user_index].reshape(1, -1))

# Get the indices of similar users
similar_users = pivot_table.index[indices.flatten()]
print(f"Users similar to user {user_id}: {similar_users}")

# You can then use the similar users' ratings to recommend items
# For simplicity, we'll recommend items that the similar users have rated highly
recommended_items = []
for sim_user in similar_users:
    if sim_user != user_id:  # Exclude the current user
        similar_user_ratings = pivot_table.loc[sim_user]
        top_rated_items = similar_user_ratings[similar_user_ratings >= 4].index.tolist()
        recommended_items.extend(top_rated_items)

# Remove items the user has already rated
recommended_items = [item for item in recommended_items if item not in pivot_table.columns[pivot_table.loc[user_id] >= 4]]

print(f"Recommended items for user {user_id}: {recommended_items}")
