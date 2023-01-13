from flask import Flask, request, jsonify, Blueprint
from config.db import db
from services.mask import Masks
from services.validator import Validator
from models.users_model import UsersModel
from datetime import datetime
# from elasticsearch import Elasticsearch
# from elasticsearch.helpers import scan

bp = Blueprint("user_route", __name__)

# e = Elasticsearch([{'host': 'http://127.0.0.1', 'port': 5000, 'scheme': ''}])



@bp.route("/", methods=["GET", "POST"])
def get_all_or_create():


    if request.method == "POST":
        data = request.get_json()
        
        validator_response = Validator.register_validator(data)
        
        if validator_response:
            return jsonify(validator_response)

        if not Validator.check_cpf_is_true(str(data['cpf'])):
            return {'erro': 'CPF inválido'},409

         
        if UsersModel.get_user_by_cpf(data['cpf']):
            return {'erro': 'CPF já cadastrado'},401

        data['cpf'] = str(Masks.cpf_clean(data['cpf']))

        data['created_at'] = datetime.now()

        data_serialized = UsersModel(**data)
        db.session.add(data_serialized)
        db.session.commit()

        return jsonify(UsersModel.serialized(data_serialized)),201

    if request.method == "GET":

        data = UsersModel.get_all_users()

        return jsonify(data),200


@bp.route("/id/<int:id>", methods=["GET"])
def get_id(id):

    query = UsersModel.get_user_by_id(str(id))
    if not query:
        return '',404
    
    return jsonify(UsersModel.serialized(query)),200
    

@bp.route("/cpf/<cpf>", methods=["GET", "DELETE", "PATCH"])
def get_cpf(cpf: str ):

    
    query = UsersModel.get_user_by_cpf(str(cpf))
    if not query:
        return '',404

    if request.method == "GET":
        
        return jsonify(UsersModel.serialized(query)),200

    if request.method == "PATCH":

        data = request.get_json()
        
        data['cpf'] = query.cpf
        data['created_at'] = query.created_at
        data['updated_at'] = datetime.now()

        for key, value in data.items():
            setattr(query, key, value)
        
        db.session.add(query)
        db.session.commit()

        return jsonify(UsersModel.serialized(query)),200
    
    if request.method == "DELETE":

        db.session.delete(query)
        db.session.commit()

        return '',200

        
        














        

    
