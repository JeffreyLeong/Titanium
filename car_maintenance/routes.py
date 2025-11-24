# titanium_site/car_maintenance/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import os

# -----------------------------
# Blueprint
# -----------------------------
car_bp = Blueprint(
    "car",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# -----------------------------
# Database Setup
# -----------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "maintenance_data.sqlite")


def init_db():
    """Initialize the SQLite database and create table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            mileage INTEGER NOT NULL,
            services TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_records():
    """Fetch all maintenance records from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM maintenance ORDER BY date DESC")
    rows = c.fetchall()
    conn.close()

    # Convert services from CSV string to list
    records = [
        {
            "id": r[0],
            "Date": r[1],
            "Mileage": r[2],
            "Services": r[3].split(","),
            "Price": r[4],
        }
        for r in rows
    ]
    return records


def add_record_to_db(date, mileage, services, price):
    """Add a maintenance record to the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO maintenance (date, mileage, services, price) VALUES (?, ?, ?, ?)",
        (date, mileage, ",".join(services), price),
    )
    conn.commit()
    conn.close()


def delete_record_from_db(record_id):
    """Delete a maintenance record by ID."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM maintenance WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()


# -----------------------------
# Routes
# -----------------------------

@car_bp.route("/", endpoint="car_home")  # explicit endpoint
def car_home():
    records = get_all_records()
    return render_template("car.html", title="Car Maintenance", records=records)


@car_bp.route("/add", methods=["GET", "POST"], endpoint="add_record")
def add_record():
    if request.method == "POST":
        date = request.form["date"]
        mileage = int(request.form["mileage"])
        services = [s.strip() for s in request.form["services"].split(",")]
        price = float(request.form["price"])

        add_record_to_db(date, mileage, services, price)
        return redirect(url_for("car.car_home"))

    return render_template("add_record.html", title="Add Maintenance Record")


@car_bp.route("/delete/<int:record_id>", methods=["POST"])
def delete_record(record_id):
    delete_record_from_db(record_id)
    return redirect(url_for("car.car_home"))


# Initialize DB when blueprint is loaded
init_db()
