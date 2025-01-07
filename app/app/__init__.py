from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    application = Flask(__name__)

    # Database configuration
    application.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JWT configuration
    application.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Initialize extensions
    db.init_app(application)
    jwt.init_app(application)

    # Import and register blueprints
    from app.routes import auth_routes, budget_routes, plaid_routes, alert_routes
    application.register_blueprint(auth_routes.bp)
    application.register_blueprint(budget_routes.bp)
    application.register_blueprint(plaid_routes.bp)
    application.register_blueprint(alert_routes.bp)

    return application 
