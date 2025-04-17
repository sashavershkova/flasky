from flask import Flask
from app.routes.cats_routes import cats_bp

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    # register blueprint
    app.register_blueprint(cats_bp)

    return app