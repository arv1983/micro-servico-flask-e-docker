from config.db import db
from sqlalchemy import Column, String, Integer,DateTime
from sqlalchemy.sql.sqltypes import Date
from validate_docbr import CPF



class UsersModel (db.Model):
    __tablename__ = "user"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    cpf = Column('cpf', String(11), nullable=False, unique=True)
    email = Column('email', String(255), nullable=False)
    phone_number = Column('phone_number', String(11), nullable=False)
    created_at = Column('created_at', DateTime)
    updated_at = Column('updated_at', DateTime)
    
    
    def serialized(self):
        data = {
            "id": self.id,
            "name": self.name,
            "cpf": CPF().mask(self.cpf),
            "email": self.email,
            "phone": self.phone_number,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
        return data

    def get_all_users():
        
        users = []
        for user in UsersModel().query.all():
            users.append(UsersModel.serialized(user))
        return users

    def get_user_by_cpf(cpf_user: str):

        user = UsersModel.query.filter_by(cpf=cpf_user).first()
        
        return user

    def get_user_by_id(id: str):

        user = UsersModel.query.filter_by(id=id).first()

        return user

    
