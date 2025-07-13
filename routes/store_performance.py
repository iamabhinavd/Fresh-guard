from flask import Blueprint, jsonify
from db import products_collection

store_performance_blueprint = Blueprint('store_performance', __name__)



@store_performance_blueprint.route('/store-performance', methods=['GET'])
def store_performance():
    """
    Tracks:
    - Total Products
    - Sold before spoilage
    - Spoiled items
    - Savings estimate
    - Simple rating based on spoilage levels
    """

    total_products = products_collection.count_documents({})
    spoiled = products_collection.count_documents({"spoiled_probability": {"$gt": 0.7}})
    sold_before_spoilage = total_products - spoiled

    # Simple savings estimate (hypothetical: Rs.50 saved per avoided spoilage)
    savings = sold_before_spoilage * 50

    # Simple performance rating logic
    if total_products == 0:
        rating = "N/A"
    elif spoiled / total_products > 0.5:
        rating = "Poor"
    elif spoiled / total_products > 0.2:
        rating = "Average"
    else:
        rating = "Good"

    return jsonify({
        "total_products": total_products,
        "spoiled": spoiled,
        "sold_before_spoilage": sold_before_spoilage,
        "estimated_savings": savings,
        "performance_rating": rating
    })
