# titanium_site/app.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
import os

db = SQLAlchemy()

def create_app():
    # Create Flask app with correct template/static folders
    app = Flask(
        __name__,
        template_folder="core/templates",
        static_folder="core/static"
    )

    # Enforce HTTPS with Talisman
    Talisman(app, force_https=True)

    # Secret key for sessions
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_key")

    # Ensure instance folder exists
    instance_path = os.path.join(app.root_path, 'instance')
    os.makedirs(instance_path, exist_ok=True)

    # SQLite database with absolute path
    db_path = os.path.join(instance_path, 'car_maintenance.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy
    db.init_app(app)

    # Import and register blueprints
    from .tip_calculator.routes import tip_bp
    from .car_maintenance.routes import car_bp

    app.register_blueprint(tip_bp, url_prefix="/tip")
    app.register_blueprint(car_bp, url_prefix="/car")

    # Home route
    @app.route("/")
    def index():
        return render_template("home.html", title="Home")

    # Create all tables
    with app.app_context():
        db.create_all()

    return app
