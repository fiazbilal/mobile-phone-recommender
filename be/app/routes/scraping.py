# app/routes/scraping.py
from flask import Blueprint, request, jsonify
from ..services.scraper import WebScraper

bp = Blueprint('scraping', __name__)

@bp.route('/scrape', methods=['POST'])
def initiate_scraping():
    websites = request.json.get('websites', [])
    scraper = WebScraper()
    results = scraper.scrape_multiple(websites)
    return jsonify(results), 200
