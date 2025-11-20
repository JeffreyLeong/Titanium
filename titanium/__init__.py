from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev_key")

    from titanium import routes
    app.register_blueprint(routes.bp)

    return app
