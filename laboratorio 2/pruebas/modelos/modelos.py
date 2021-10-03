from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Pruebas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(128))
    resultado = db.Column(db.Boolean)

   
class PruebasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pruebas
        load_instance = True