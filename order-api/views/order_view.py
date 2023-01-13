import requests
import json
from flask import Flask, request, jsonify, Blueprint
from config.db import db
from services.validator import Validator
from models.order_model import OrderModel
from datetime import datetime
from flask import request
from config.server import ConfigServer


bp = Blueprint("post_route", __name__)


@bp.route("/", methods=["POST","GET"])
def create_order():

    if request.method == "POST":
        data = request.get_json()
        validator_response = Validator.order_validator(data)
        if validator_response: 
            return jsonify(validator_response)

        response = requests.get(f"{ConfigServer.server}:{ConfigServer.port}/id/{data['user_id']}")

        if response.status_code != 200:
            return jsonify({'Error': 'User id not found'}),404


        data['total_value'] = data['item_quantity'] * data['item_price']

        data['created_at'] = datetime.now()

        data_serialized = OrderModel(**data)
        db.session.add(data_serialized)
        db.session.commit()

        return '',201

    if request.method == "GET":

        data = OrderModel.get_all_orders()

        return jsonify(data),200        



@bp.route("/order/<int:id>", methods=["DELETE", "PATCH", "GET"])
def order(id):
    query = OrderModel.get_order_by_id(id)

    if not query:
       return jsonify({'Error': 'Order not found.'}),404

    if request.method == "DELETE":
        db.session.delete(query)
        db.session.commit()
        return '',200
    
    if request.method == "GET":
        return jsonify(OrderModel.serialized(query))

    if request.method == "PATCH":
        
        data = request.get_json()
        
        data['user_id'] = query.user_id
        data['created_at'] = query.created_at
        data['updated_at'] = datetime.now()
       
        if not 'item_price' in data.keys():
            data['item_price'] = query.item_price

        if not 'item_quantity' in data.keys():
            data['item_quantity'] = query.item_quantity

        data['total_value'] = data['item_quantity'] * data['item_price']
        
        for key, value in data.items():
            setattr(query, key, value)
          
        db.session.add(query)
        db.session.commit()

        return jsonify(OrderModel.serialized(query)),200


@bp.route("/order/cpf/<cpf>", methods=["GET"])        
def get_order_cpf(cpf: str):
    # return jsonify(cpf)
    
    response = requests.get(f"{ConfigServer.server}:{ConfigServer.port}/cpf/{cpf}")
    
    if response.status_code != 200:
        return jsonify({'Error': 'Cpf not found'}),404

    query = OrderModel.get_all_orders_by_id(response.json()['id'])
    
    return jsonify(query)





        
        














        

    
