from flask import Blueprint

tip_bp = Blueprint(
    'tip',
    __name__,
    template_folder="templates"
)


from . import routes
