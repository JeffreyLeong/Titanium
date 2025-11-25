from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class CarRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)   # ISO date string
    mileage = db.Column(db.Integer, nullable=False)
    services = db.Column(db.String(1000), nullable=False)  # comma-separated
    price = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def service_list(self):
        # returns list of services
        return [s.strip() for s in (self.services or "").split(",") if s.strip()]
