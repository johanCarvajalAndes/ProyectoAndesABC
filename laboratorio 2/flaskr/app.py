from flaskr import create_app
from flask_restful import Api
from .modelos import db
from .vistas import VistaLogIn, VistaToken, VistaUsuario
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(VistaLogIn, '/logIn')
api.add_resource(VistaToken, '/token/<int:id_token>')
api.add_resource(VistaUsuario, '/user/<int:id_usuario>')

jwt = JWTManager(app)