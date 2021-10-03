from flask import request
from faker import Faker
from flaskr.modelos.modelos import TokenSchema, Usuario
from ..modelos import db, Pruebas, PruebasSchema
from flask_restful import Resource
import requests 
from flaskr.modelos import TokenSchema
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
    def tokenRandom(self):
        tokenList = []
        faker = Faker()
        for i in range(5):
            tokenList.append(faker.password(length=260))
        return tokenList
    
    def cargarUsuarios(self):
        with open("test_usuarios.json") as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        db.session.query(Usuario).delete()
        
        for i in range(len(jsonObject)):
            usuario = jsonObject[i]
            nombre = usuario['user']
            contrasena = usuario['pass']
            permiso = usuario['permiso']
            nuevoUsuario = Usuario(nombre=nombre, contrasena=contrasena, permiso=permiso)

            db.session.add(nuevoUsuario)
            db.session.commit()

    def get(self):
        for j in range(1,6):   
            arreglo = self.tokenRandom()
            url = 'http://127.0.0.1:5000/token/'+str(j)
            token = requests.get(url)
            data = token.json()
            valorToken = data['token']
            valorUsuario = data['usuario']
            arreglo.append(valorToken)

            for i in range(len(arreglo)):
                tokenBearer = 'Bearer ' + arreglo[i]
                cabeceras = {'Authorization': tokenBearer}
                factura =  'http://127.0.0.1:5001/facturas'
                content = requests.get(factura, headers=cabeceras)
                contenido = content.json()

                if len(contenido) == 16:
                    resultado = False
                    fecha = datetime.now()
                    nueva_prueba = Pruebas(fecha=fecha, resultado=resultado)
                    db.session.add(nueva_prueba)
                    db.session.commit()
                    print("PERMISO DENEGADO", 404)

                elif len(contenido) == 1:
                    resultado = False
                    fecha = datetime.now()
                    nueva_prueba = Pruebas(fecha=fecha, resultado=resultado)
                    db.session.add(nueva_prueba)
                    db.session.commit()
                    print("USUARIO NO AUTORIZADO", 404)

                else:
                    resultado = True
                    fecha = datetime.now()
                    nueva_prueba = Pruebas(fecha=fecha, resultado=resultado)
                    db.session.add(nueva_prueba)
                    db.session.commit()
                    print( "El usuario ", valorUsuario, " pudo leer las facturas ", 200)
                
            arreglo.clear()

    
    