"""Application configuration."""

import os


class Config:
    """Flask application configuration."""

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///pos.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
