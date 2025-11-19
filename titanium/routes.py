from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html', title="Titanium Home")

@bp.route('/tip')
def tip_calculator():
    return render_template('tip.html', title="Tip Calculator")