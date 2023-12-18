from flask import Flask
from models.category import db
from flask_migrate import Migrate
from routes.category_routes import category_blueprint
from routes.customer_routes import customer_blueprint
from routes.product_routes import product_blueprint
from routes.order_routes import order_blueprint
from routes.order_history_route import order_history_blueprint

# Function to create the Flask app
def create_app():
    app = Flask(__name__)
    
    # Load configuration from the "config" module
    app.config.from_object("config")

    # Initialize the database with the Flask app
    db.init_app(app)

    return app

# Create the Flask app instance
app = create_app()

# Register blueprints for different parts of the application
app.register_blueprint(category_blueprint, url_prefix="/category")
app.register_blueprint(customer_blueprint, url_prefix="/customer")
app.register_blueprint(product_blueprint, url_prefix="/product")
app.register_blueprint(order_blueprint, url_prefix="/order")
app.register_blueprint(order_history_blueprint, url_prefix="/order-history")

# Initialize the Flask-Migrate extension for database migrations
migrate = Migrate(app, db)

# Run the app only if the script is executed directly (not imported)
if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)