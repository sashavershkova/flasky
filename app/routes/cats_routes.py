from flask import Blueprint, abort, make_response, request, Response
from app.models.cats import Cat
from ..db import db

cats_bp = Blueprint("cats_bp", __name__, url_prefix = "/cats")

# POST ONE CAT
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

# GET ALL CATS
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

# GET ONE CAT
@cats_bp.get("/<cat_id>")
def get_one_cat(cat_id):
    cat = validate_cat(cat_id)

    return dict(
        id = cat.id,
        name = cat.name,
        color = cat.color,
        breed = cat.breed
    )

# UPDATE ONE CAT
@cats_bp.put("/<cat_id>")
def update_one_cat(cat_id):
    cat = validate_cat(cat_id)
    request_body = request.get_json()
    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.breed = request_body["breed"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

# DELETE ONE CAT
@cats_bp.delete("/<cat_id>")
def delete_one_cat(cat_id):
    cat = validate_cat(cat_id)

    db.session.delete(cat)
    db.session.commit()

    return Response(status=204, mimetype="application/json")



# HELPER FUNCTION VALIDATING CAT
def validate_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except:
        response = {"message": f"id {cat_id} is invalid"}
        abort(make_response(response, 400))

    query = db.select(Cat).where(Cat.id == cat_id)
    cat = db.session.scalar(query)
    
    if not cat:
        response = {"message": f"cat with id {cat_id} not found"}
        abort(make_response(response, 404))

    return cat

