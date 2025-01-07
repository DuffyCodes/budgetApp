from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token
import datetime

# Hash password
def hash_password(password):
    return bcrypt.hash(password)

# Verify password
def verify_password(hashed_password, password):
    return bcrypt.verify(password, hashed_password)

# Create JWT token
def create_access_token(identity):
    return create_access_token(identity=identity, expires_delta=datetime.timedelta(days=1))