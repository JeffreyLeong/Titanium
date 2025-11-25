from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register core blueprint
    from .core.routes import core_bp
    app.register_blueprint(core_bp)

    # Register Car Maintenance blueprint
    from .car_maintenance.routes import car_bp
    app.register_blueprint(car_bp, url_prefix="/car")

    return app
