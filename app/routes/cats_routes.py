from flask import Blueprint
from app.models.cats import Cat, cats

cats_bp = Blueprint("cats_bp", __name__, url_prefix = "/cats")

@cats_bp.get("")
def get_all_cats():
    response_cats = []
    for cat in cats:
        response_cats.append(dict(
            id = cat.id,
            name = cat.name,
            color = cat.color,
            breed = cat.breed
        ))
    return response_cats

