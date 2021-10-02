from pruebas import create_app
from flask_restful import Resource, Api
from flask import Flask, request 
from .modelos import db
from .vistas.vistas import VistaNuevaPrueba, VistaPruebas, VistaPrueba, VistaRequest
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
import requests

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

#PRUEBA

api = Api(app)

api.add_resource(VistaPruebas,'/pruebas')
api.add_resource(VistaPrueba,'/prueba/<int:id_prueba>')
api.add_resource(VistaNuevaPrueba,'/prueba')
api.add_resource(VistaRequest,'/tokens')

jwt = JWTManager(app)

