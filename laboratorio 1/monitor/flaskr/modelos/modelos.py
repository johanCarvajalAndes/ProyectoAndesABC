from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(128))
    descripcion = db.Column(db.String(128))
    fecha = db.Column(db.String(128))