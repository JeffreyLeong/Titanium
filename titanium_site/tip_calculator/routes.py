from flask import render_template
from . import tip_bp  # import the existing blueprint

# Rename endpoint to tip_home
@tip_bp.route("/", endpoint="tip_home")
def tip_calculator():
    return render_template("tip.html", title="Tip Calculator")
