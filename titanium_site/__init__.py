from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Car Maintenance Blueprint
    from .car_maintenance.routes import car_bp
    app.register_blueprint(car_bp, url_prefix="/car")

    # You can register other blueprints, e.g., tip_calculator, core, etc.
    # from .tip_calculator.routes import tip_bp
    # app.register_blueprint(tip_bp, url_prefix="/tip")

    return app
