from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Pastikan folder data ada untuk SQLite
    os.makedirs('/app/data', exist_ok=True) if os.path.exists('/app') else None

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Silakan login terlebih dahulu.'
    login_manager.login_message_category = 'warning'

    from app.routes.auth import auth_bp
    from app.routes.soal import soal_bp
    from app.routes.quiz import quiz_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(soal_bp)
    app.register_blueprint(quiz_bp)

    with app.app_context():
        db.create_all()

    return app
