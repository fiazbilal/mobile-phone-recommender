import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example data: Mobiles with features like genre and keywords
data = {
    'Mobile_id': [1, 2, 3, 4, 5],
    'title': ['Mobile A', 'Mobile B', 'Mobile C', 'Mobile D', 'Mobile E'],
    'genre': ['Action|Adventure', 'Action|Sci-Fi', 'Sci-Fi|Thriller', 'Action|Adventure', 'Action|Thriller'],
    'keywords': ['hero, battle, fight', 'space, alien, fight', 'space, mystery, thriller', 'hero, battle, adventure', 'thriller, mystery, fight']
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Combine genre and keywords into a single text column for content comparison
df['content'] = df['genre'] + " " + df['keywords']

# Create a TF-IDF Vectorizer to transform the content into a numerical format
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit the TF-IDF model to the content data
tfidf_matrix = tfidf_vectorizer.fit_transform(df['content'])

# Calculate the cosine similarity between items based on their content
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get Mobile recommendations based on content similarity
def get_recommendations(Mobile_title):
    # Get the index of the Mobile that matches the title
    idx = df[df['title'] == Mobile_title].index[0]
    
    # Get the pairwise similarity scores for the given Mobile with all other Mobiles
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the Mobiles based on similarity scores (highest first)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the most similar Mobiles (excluding the input Mobile)
    sim_scores = sim_scores[1:3]  # Top 2 similar Mobiles
    Mobile_indices = [i[0] for i in sim_scores]
    
    # Return the recommended Mobile titles
    return df['title'].iloc[Mobile_indices]

# Get recommendations for "Mobile A"
recommended_Mobiles = get_recommendations("Mobile A")
print(f"Recommended Mobiles for 'Mobile A': {recommended_Mobiles}")
