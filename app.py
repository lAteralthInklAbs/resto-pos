"""Flask application factory for RestoPoS."""
from flask import Flask
from src.config import Config
from src.models import db
from src.routes import bp
from src.seed_data import seed_menu_items


def create_app(config_class=Config):
    """Create and configure Flask application.

    Args:
        config_class: Configuration class to use.

    Returns:
        Configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(bp)

    # Create tables and seed data
    with app.app_context():
        db.create_all()
        seed_menu_items()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
