# titanium_site/app.py

from flask import Flask, render_template
import os
from flask_talisman import Talisman
from flask_sqlalchemy import SQLAlchemy

# Initialize database globally
db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder="core/templates",
        static_folder="core/static",
    )

    # Security settings
    Talisman(app, force_https=True)

    # Secret key
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_key")

    # SQLite configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_maintenance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB with app
    db.init_app(app)

    # Register blueprints
    from .tip_calculator.routes import tip_bp
    from .car_maintenance.routes import car_bp

    app.register_blueprint(tip_bp, url_prefix="/tip")
    app.register_blueprint(car_bp, url_prefix="/car")

    @app.route("/")
    def index():
        return render_template("home.html", title="Home")

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
