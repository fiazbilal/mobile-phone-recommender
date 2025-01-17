import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

class PhoneRecommender:
    def __init__(self):
        # Initialize the phone data
        self.data = pd.DataFrame([
            ["POCO M4 5G (Power Black, 64 GB)", 12999, 4, 50, "Mediatek Dimensity 700 Processor", 5000, 4.2, "Poco"],
            ["POCO M4 5G (Cool Blue, 64 GB)", 12999, 4, 50, "Mediatek Dimensity 700 Processor", 5000, 4.2, "Poco"],
            ["SAMSUNG Galaxy F13 (Nightsky Green, 64 GB)", 10999, 4, 50, "Exynos 850 Processor", 6000, 4.4, "Samsung"],
            ["SAMSUNG Galaxy F13 (Waterfall Blue, 64 GB)", 10999, 4, 50, "Exynos 850 Processor", 6000, 4.4, "Samsung"],
            ["MOTOROLA g52 (Charcoal Grey, 128 GB)", 12999, 6, 50, "Qualcomm Snapdragon 680 Processor", 5000, 4.2, "Moto"],
            ["POCO M4 5G (Cool Blue, 128 GB)", 14999, 6, 50, "Mediatek Dimensity 700 Processor", 5000, 4.2, "Poco"],
            ["SAMSUNG Galaxy S21 FE 5G (Graphite, 128 GB)", 38999, 8, 50, "Mediatek Dimensity 700 Processor", 4000, 4.4, "Samsung"],
            ["realme 10 Pro 5G (Hyperspace, 128 GB)", 22999, 6, 50, "Qualcomm Snapdragon 695 Processor", 5000, 4.3, "Realme"],
            ["POCO X5 5G (Jaguar Black, 128 GB)", 17999, 6, 50, "Mediatek Dimensity 700 Processor", 5000, 4.2, "Poco"]
        ], columns=["Model", "Prices", "RAM", "Camera", "Processor", "Battery", "Ratings", "Brand"])
        
        # Create processor encoding
        self.processor_encoding = {
            "Mediatek Dimensity 700 Processor": 1,
            "Exynos 850 Processor": 2,
            "Qualcomm Snapdragon 680 Processor": 3,
            "Qualcomm Snapdragon 695 Processor": 4
        }
        
        # Create brand encoding
        self.brand_encoding = {brand: idx for idx, brand in enumerate(self.data['Brand'].unique())}
        
        # Prepare the feature matrix
        self.prepare_features()
        
    def prepare_features(self):
        """Prepare and normalize features for similarity calculation"""
        # Create feature matrix
        feature_data = pd.DataFrame({
            'price': self.data['Prices'],
            'ram': self.data['RAM'],
            'battery': self.data['Battery'],
            'ratings': self.data['Ratings'],
            'processor': self.data['Processor'].map(self.processor_encoding),
            'brand': self.data['Brand'].map(self.brand_encoding)
        })
        
        # Normalize features
        scaler = MinMaxScaler()
        self.features_normalized = scaler.fit_transform(feature_data)
        
        # Calculate similarity matrix
        self.similarity_matrix = cosine_similarity(self.features_normalized)
    
    def get_recommendations(self, phone_model, n_recommendations=3):
        """Get phone recommendations based on similarity to input phone"""
        try:
            # Find the index of the input phone
            phone_idx = self.data[self.data['Model'].str.contains(phone_model, case=False)].index[0]
            
            # Get similarity scores
            similarity_scores = self.similarity_matrix[phone_idx]
            
            # Get indices of most similar phones (excluding the input phone)
            similar_indices = similarity_scores.argsort()[::-1][1:n_recommendations+1]
            
            # Get recommended phones with similarity scores
            recommendations = []
            for idx in similar_indices:
                phone_data = self.data.iloc[idx]
                similarity = similarity_scores[idx]
                recommendations.append({
                    'model': phone_data['Model'],
                    'price': phone_data['Prices'],
                    'ram': phone_data['RAM'],
                    'battery': phone_data['Battery'],
                    'ratings': phone_data['Ratings'],
                    'similarity_score': round(similarity * 100, 2)
                })
            
            return recommendations
        
        except IndexError:
            return f"Phone model '{phone_model}' not found in database."
    
    def get_recommendations_by_budget(self, budget, n_recommendations=3):
        """Get phone recommendations within a specific budget"""
        # Filter phones within budget
        budget_phones = self.data[self.data['Prices'] <= budget]
        
        if budget_phones.empty:
            return f"No phones found within budget of {budget}"
        
        # Sort by ratings and specs
        budget_phones['score'] = (
            budget_phones['Ratings'] * 0.4 +  # Weight for ratings
            (budget_phones['RAM'] / 8) * 0.3 +  # Weight for RAM (normalized to 8GB)
            (budget_phones['Battery'] / 6000) * 0.3  # Weight for battery (normalized to 6000mAh)
        )
        
        # Get top recommendations
        recommendations = []
        for _, phone in budget_phones.nlargest(n_recommendations, 'score').iterrows():
            recommendations.append({
                'model': phone['Model'],
                'price': phone['Prices'],
                'ram': phone['RAM'],
                'battery': phone['Battery'],
                'ratings': phone['Ratings'],
                'score': round(phone['score'] * 100, 2)
            })
        
        return recommendations

# Example usage
recommender = PhoneRecommender()

# Get recommendations similar to a specific phone
print("\nRecommendations similar to POCO M4:")
recommendations = recommender.get_recommendations("POCO M4")
for rec in recommendations:
    print(f"\nModel: {rec['model']}")
    print(f"Price: ₹{rec['price']}")
    print(f"RAM: {rec['ram']}GB")
    print(f"Battery: {rec['battery']}mAh")
    print(f"Rating: {rec['ratings']}")
    print(f"Similarity Score: {rec['similarity_score']}%")

# Get recommendations within a budget
print("\nRecommendations within ₹15000:")
budget_recommendations = recommender.get_recommendations_by_budget(15000)
for rec in budget_recommendations:
    print(f"\nModel: {rec['model']}")
    print(f"Price: ₹{rec['price']}")
    print(f"RAM: {rec['ram']}GB")
    print(f"Battery: {rec['battery']}mAh")
    print(f"Rating: {rec['ratings']}")
    print(f"Score: {rec['score']}%")