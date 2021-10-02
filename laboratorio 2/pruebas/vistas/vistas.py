from flask import request
from faker import Faker
from flaskr.modelos.modelos import TokenSchema
from ..modelos import db, Pruebas, PruebasSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import sys 
import requests 
from flaskr.modelos import Token, TokenSchema
from datetime import datetime
import json


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
    tokenList = []

    def tokenRandom(self):
        global tokenList
        faker = Faker()
        for i in range(5):
            self.tokenList.append(faker.password(length=260))

    def get(self):
        global tokenList
        self.tokenRandom()
        for j in range(1,3):   
            url = 'http://127.0.0.1:5000/token/'+str(j)
            token = requests.get(url)
            data = token.json()
            valorToken = data['token']
            self.tokenList.append(valorToken)
            for i in range(len(self.tokenList)):
                tokenBearer = 'Bearer ' + self.tokenList[i]
                cabeceras = {'Authorization': tokenBearer} 
                content = requests.get('http://127.0.0.1:5001/facturas', headers=cabeceras)

                if (content):
                    resultado = True
                    fecha = datetime.now()
                    nueva_prueba = Pruebas(fecha=fecha, resultado=resultado)
                    db.session.add(nueva_prueba)
                    db.session.commit()
                    #return "El usuario existe", 200
                    print( "El usuario existe", 200)

                else:
                    resultado = False
                    fecha = datetime.now()
                    nueva_prueba = Pruebas(fecha=fecha, resultado=resultado)
                    db.session.add(nueva_prueba)
                    db.session.commit()
                    #return "El usuario no existe", 404
                    print("El usuario no existe", 404)
        

    
    