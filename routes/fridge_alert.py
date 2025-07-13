from flask import Blueprint, jsonify
from db import products_collection

fridge_alert_blueprint = Blueprint('fridge_alert', __name__)

# MongoDB connection
fridge_alert_blueprint = Blueprint('fridge_alert', __name__)

@fridge_alert_blueprint.route('/fridge-alerts', methods=['GET'])
def fridge_alerts():
    """
    Simulate fridge failure by checking for abnormally high temperatures (>15°C).
    """

    risky_products = list(products_collection.find({"temp": {"$gt": 15}}))

    alerts = []
    for product in risky_products:
        alerts.append({
            "product_name": product["product_name"],
            "category": product.get("category", "Other"),
            "temp": product["temp"],
            "message": "Potential fridge failure! Temperature exceeds safe limit."
        })

    return jsonify({
        "alerts": alerts,
        "count": len(alerts)
    })
