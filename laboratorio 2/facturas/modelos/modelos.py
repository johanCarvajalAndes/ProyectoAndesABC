from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Facturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    concepto = db.Column(db.String(128))
    nombre = db.Column(db.String(128))
    fecha = db.Column(db.String(128))
    valor = db.Column(db.String(128))
   
class FacturasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Facturas
        include_relationships = True
        load_instance = True