
from flask import Flask

def init_app(app: Flask):
    from .users_view import bp as users
    app.register_blueprint(users)

