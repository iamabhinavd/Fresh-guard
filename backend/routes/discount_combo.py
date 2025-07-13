from flask import Blueprint, jsonify
from db import products_collection  
discount_blueprint = Blueprint('discount_combo', __name__)

# MongoDB connection
discount_blueprint = Blueprint('discount_combo', __name__)

@discount_blueprint.route("/analyze-discounts-combos", methods=['GET'])
def analyze_discounts():
    products = list(products_collection.find())

    response = []
    category_map = {}

    for p in products:
        spoilage = p.get('spoiled_probability', 0)

        # Assign discount
        if spoilage > 0.8:
            discount = "30%"
        elif spoilage > 0.5:
            discount = "15%"
        else:
            discount = "None"

        # Save to DB
        products_collection.update_one(
            {'_id': p['_id']},
            {"$set": {"suggested_discount": discount}}
        )

        # Prepare for combo grouping
        if spoilage > 0.6:
            cat = p.get('category', 'Other')
            if cat not in category_map:
                category_map[cat] = []
            category_map[cat].append(p['product_name'])

        response.append({
            "product_name": p['product_name'],
            "spoilage": round(spoilage * 100, 1),
            "discount": discount
        })

    # Generate combo bundles
    combos = []
    for cat, items in category_map.items():
        if len(items) >= 2:
            combos.append({
                "category": cat,
                "combo_items": items
            })

    return jsonify({
        "products": response,
        "combos": combos
    })
