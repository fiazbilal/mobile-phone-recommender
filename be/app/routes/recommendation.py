# app/routes/recommendation.py
from flask import Blueprint, request, jsonify
from ..services.ml_model import MobileRecommendationModel

bp = Blueprint('recommendation', __name__)

@bp.route('/recommend', methods=['POST'])
def get_recommendations():
    user_preferences = request.json
    model = MobileRecommendationModel()
    recommendations = model.predict(user_preferences)
    return jsonify(recommendations), 200
