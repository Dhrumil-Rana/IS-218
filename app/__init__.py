from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile('config.py')

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app
