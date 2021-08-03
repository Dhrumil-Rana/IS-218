from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all

db = SQLAlchemy()
patch_all()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        # Register Blueprints
        app.register_blueprint(routes.views)
        # app.register_blueprint(admin.admin_bp)
        db.create_all()
        return app
