from flaskr.vistas.vistas import VistaFacturas, VistaFactura, VistaNuevaFactura
from flaskr import create_app
from flask_restful import Api
from .modelos import db
from flask_cors import CORS
import setproctitle

setproctitle.setproctitle('consultas')


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#PRUEBA

api = Api(app)

api.add_resource(VistaFacturas,'/facturas')
api.add_resource(VistaFactura,'/factura/<int:id_factura>')
api.add_resource(VistaNuevaFactura,'/factura')



