from flask import request
from ..modelos import db, Facturas, FacturasSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import sys
import requests

factura_schema = FacturasSchema()

class VistaFacturas(Resource):
    
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        try:
            url = 'http://127.0.0.1:5000/user/'+str(current_user)
            permiso = requests.get(url)
            data = permiso.json()
            valorPermiso = int(data['permiso'])
            valorNombre = data['nombre']
            if valorPermiso == 1:
                print("El usuario ", valorNombre, " tiene permisos de lectura")
                return [factura_schema.dump(f) for f in Facturas.query.all()]
            else:
                return "PERMISO DENEGADO"
        except:
            return "USUARIO NO EXISTE"

class VistaNuevaFactura(Resource):

    def post(self):
        nueva_factura = Facturas(concepto=request.json["concepto"], nombre=request.json["nombre"], fecha=request.json["fecha"], valor=request.json["valor"])
        db.session.add(nueva_factura)
        db.session.commit()
        return 'Factura creada exitosamente', 201

class VistaFactura(Resource):
    
    def get(self, id_factura):
        return factura_schema.dump(Facturas.query.get_or_404(id_factura))

    def put(self, id_factura):
        factura = Facturas.query.get_or_404(id_factura)
        factura.concepto = request.json.get("concepto",factura.concepto)
        factura.nombre = request.json.get("nombre",factura.nombre)
        factura.fecha = request.json.get("fecha",factura.fecha)
        factura.valor = request.json.get("valor",factura.valor)
        db.session.commit()
        return factura_schema.dump(factura)
 
    def delete(self, id_factura):
        factura = Facturas.query.get_or_404(id_factura)
        db.session.delete(factura)
        db.session.commit()
        return '',204