from flask import Blueprint, abort, make_response, request
from app.models.cats import Cat
from ..db import db

cats_bp = Blueprint("cats_bp", __name__, url_prefix = "/cats")

@cats_bp.post("")
def add_new_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    breed = request_body["breed"]

    new_cat = Cat(name=name, color=color, breed=breed)
    db.session.add(new_cat)
    db.session.commit()

    response_new_cat = {
        "id": new_cat.id,
        "name": new_cat.name,
        "color": new_cat.color,
        "breed": new_cat.breed,
    }

    return response_new_cat, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)

    response_cats = []
    for cat in cats:
        response_cats.append(dict(
            id = cat.id,
            name = cat.name,
            color = cat.color,
            breed = cat.breed
        ))
        
    return response_cats

# @cats_bp.get("/<id>")
# def get_one_cat(id):
#     cat = validate_cat(id)
#     return dict(
#         id = cat.id,
#         name = cat.name,
#         color = cat.color,
#         breed = cat.breed
#     )

# def validate_cat(id):
#     try:
#         id = int(id)
#     except:
#         response = {"message": f"id {id} is invalid"}
#         abort(make_response(response, 400))

#     for cat in cats:
#         if cat.id == id:
#             return cat
    
#     response = {"message": f"cat with id {id} not found"}
#     abort(make_response(response, 404))

