import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'eduquiz-secret-2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///eduquiz.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False