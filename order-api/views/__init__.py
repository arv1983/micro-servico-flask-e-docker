
from flask import Flask

def init_app(app: Flask):
    from .order_view import bp as order
    app.register_blueprint(order)

