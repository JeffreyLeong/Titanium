from flask import Flask
from car_maintenance import car_bp

app = Flask(__name__)

# Register your car maintenance blueprint
app.register_blueprint(car_bp)

@app.route("/")
def home():
    return "Welcome to Titanium Site!"

if __name__ == "__main__":
    app.run(debug=True)
