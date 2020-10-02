# app/__init__.py

"""
Entry point for our Application
Bolierplate Code:
https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
"""

from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SQL Utilities',
          version='0.0.1',
          description='SQL Utilities made in Flask-RestPlus'
          )

api.add_namespace(user_ns, path='/user')
