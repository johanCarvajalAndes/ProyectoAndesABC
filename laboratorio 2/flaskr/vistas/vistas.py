from flask import request
from flaskr.modelos.modelos import TokenSchema
from ..modelos import db,Usuario, UsuarioSchema, Token, TokenSchema
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask import request
from flaskr.modelos.modelos import Usuario, db

usuarioBD = Usuario()
usuario_schema = UsuarioSchema()
token_schema = TokenSchema()

class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre == request.json["nombre"], Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity = usuario.id)
            token = Token(token = token_de_acceso, usuario = usuario.id)
            db.session.add(token)
            db.session.commit()
            return {"mensaje":"Inicio de sesión exitoso", "token": token_de_acceso}

class VistaToken(Resource):

    def get(self, id_token):
        token = Token.query.filter(Token.usuario == id_token).first()
        return token_schema.dump(token)

class VistaUsuario(Resource):

    def get(self, id_usuario):
        usuario = Usuario.query.filter(Usuario.id == id_usuario).first()
        return usuario_schema.dump(usuario)