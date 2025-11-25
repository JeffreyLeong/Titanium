from flask import Blueprint
from .models import db

car_bp = Blueprint(
    "car",
    __name__,
    template_folder="templates",
    static_folder="static"
)

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///car_maintenance.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import register_routes
    register_routes(car_bp)

    app.register_blueprint(car_bp, url_prefix="/car")
