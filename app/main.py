from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT configuration
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import and register routes
from routes import auth_routes, budget_routes, plaid_routes, alert_routes
app.register_blueprint(auth_routes.bp)
app.register_blueprint(budget_routes.bp)
app.register_blueprint(plaid_routes.bp)
app.register_blueprint(alert_routes.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)