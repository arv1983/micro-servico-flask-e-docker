from flask import Flask
from flask import Blueprint
from environs import Env
from config import db
import views

bp = Blueprint('user', __name__, url_prefix='/api')

def create_app() -> Flask:
    app = Flask(__name__)
    env = Env()
    env.read_env()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@dbpostgres:5432/dbserasa'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@0.0.0.0:5432/dbserasa'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    db.init_app(app)
    # migrate.init_app(app)
    views.init_app(app)

    

    return app