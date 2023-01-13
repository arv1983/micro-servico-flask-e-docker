from flask import Flask, request, jsonify
from config.db import db
from sqlalchemy import Column, DateTime, String, Integer, Float
from sqlalchemy.sql.sqltypes import Date



class OrderModel (db.Model):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, nullable=False)
    item_description = Column('item_description', String(255), nullable=False)
    item_quantity = Column('item_quantity', Float, nullable=False)
    item_price = Column('item_price', Float, nullable=False)
    total_value = Column('total_value', Float, nullable=False)
    created_at = Column('created_at', DateTime)
    updated_at = Column('updated_at', DateTime)
    
    def serialized(self):
        data = {
            "id": self.id,
            "user id": self.user_id,
            "item_description": self.item_description,
            "item_quantity": self.item_quantity,
            "item_price": self.item_price,
            "total_value": self.total_value,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return data


    def get_order_by_id(id):

        order = OrderModel.query.filter_by(id=str(id)).first()

        return order

    def get_all_orders_by_id(id):        
        orders = []

        for order in OrderModel.query.filter_by(user_id=id).all():
            orders.append(OrderModel.serialized(order))

        return orders

    def get_all_orders():        
        orders = []

        for order in OrderModel.query.all():
            orders.append(OrderModel.serialized(order))

        return orders

