from flask import Flask, request, jsonify
from config.db import db
from sqlalchemy import Column, Date, ForeignKey, String, Integer, Float
from sqlalchemy.sql.sqltypes import DateTime


class OrderModel (db.Model):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('user.id'), nullable=False)
    item_description = Column('item_description', String(255), nullable=False)
    item_quantity = Column('item_quantity', Float, nullable=False)
    item_price = Column('item_price', Float, nullable=False)
    total_value = Column('total_value', Float, nullable=False)
    created_at = Column('created_at', DateTime)
    updated_at = Column('updated_at', DateTime)
    
