from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'enter_compression_formula_2991'

    from titanium import routes
    app.register_blueprint(routes.bp)

    return app
