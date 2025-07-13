from flask import Flask
from flask_cors import CORS
from routes.prediction import prediction_blueprint
from routes.discount_combo import discount_blueprint
from routes.movement_alert import movement_blueprint
from routes.fridge_alert import fridge_alert_blueprint
from routes.store_performance import store_performance_blueprint


app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(prediction_blueprint)
app.register_blueprint(discount_blueprint)
app.register_blueprint(movement_blueprint)
app.register_blueprint(fridge_alert_blueprint)
app.register_blueprint(store_performance_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
