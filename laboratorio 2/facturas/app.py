from . import create_app
from flask_restful import Api
from .modelos import db
from .vistas.vistas import VistaFacturas, VistaFactura, VistaNuevaFactura
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

#PRUEBA

api = Api(app)

api.add_resource(VistaFacturas,'/facturas')
api.add_resource(VistaFactura,'/factura/<int:id_factura>')
api.add_resource(VistaNuevaFactura,'/factura')

jwt = JWTManager(app)

