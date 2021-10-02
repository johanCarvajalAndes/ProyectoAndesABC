from flask import request

from flaskr.modelos.modelos import TokenSchema
from ..modelos import db, Pruebas, PruebasSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import sys 
import requests 
from flaskr.modelos import Token, TokenSchema
from datetime import date


prueba_schema = PruebasSchema()
token_schema = TokenSchema()

class VistaPruebas(Resource):
    
    def get(self):
        return [prueba_schema.dump(f) for f in Pruebas.query.all()]

class VistaNuevaPrueba(Resource):

    def post(self):
        nueva_prueba = Pruebas(fecha=request.json["fecha"], hora=request.json["hora"], resultado=request.json["resultado"])
        db.session.add(nueva_prueba)
        db.session.commit()
        return 'Factura creada exitosamente', 201

class VistaPrueba(Resource):
    
    def get(self, id_factura):
        return prueba_schema.dump(Pruebas.query.get_or_404(id_factura))

    def put(self, id_prueba):
        prueba = Pruebas.query.get_or_404(id_prueba)
        prueba.fecha = request.json.get("fecha",prueba.fecha)
        prueba.hora = request.json.get("hora",prueba.hora)
        prueba.resultado = request.json.get("resultado",prueba.resultado)

        db.session.commit()
        return prueba_schema.dump(prueba)
 
    def delete(self, id_prueba):
        prueba = Pruebas.query.get_or_404(id_prueba)
        db.session.delete(prueba)
        db.session.commit()
        return '',204

class VistaRequest(Resource):


    def get(self, id_token):
        # usuario = "1"
        #parametros = {'usuario': "1"}
        token = requests.get('http://127.0.0.1:5000/token/1')
        token.json()
        #print(token)
        # tokenBearer = 'Bearer' + token
        # print(tokenBearer)
        # cabeceras = {'Authorization': tokenBearer} 
        # content = requests.get('http://127.0.0.1:5000/facturas', headers=cabeceras)
        # print(content)

        # if (content):
        #     resultado = True
        #     fecha = date.today()
        #     nueva_prueba = Pruebas(fecha=request.json[fecha], resultado=request.json[resultado])
        #     db.session.add(nueva_prueba)
        #     db.session.commit()
        #     return {"mensaje":"Inicio de sesión exitoso", "token": token}

        # else:
        #     resultado = False
        #     fecha = date.today()
        #     nueva_prueba = Pruebas(fecha=request.json[str(fecha)], resultado=request.json[str(resultado)])
        #     db.session.add(nueva_prueba)
        #     db.session.commit()
        #     return "El usuario no existe", 404
        
        return token_schema.dump(token)
        

    
    