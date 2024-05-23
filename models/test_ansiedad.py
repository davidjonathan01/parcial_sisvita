from utils.db import db
from datetime import datetime

class Test_Ansiedad(db.Model):
    __tablename__ = 'test_ansiedad'
    id_test_ansiedad = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(300), nullable=False)
    n_preguntas = db.Column(db.Integer, nullable=False)
    detalle_escalas = db.Column(db.String(500), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    idiomas_disponibles = db.Column(db.String(300), nullable=False)
    fecha_actualizacion = db.Column(db.Date, nullable=False)
    
    def __init__(self, nombre, descripcion, n_preguntas, detalle_escalas, version, idiomas_disponibles, fecha_actualizacion=datetime.now()):
        self.nombre = nombre
        self.descripcion = descripcion
        self.n_preguntas = n_preguntas
        self.detalle_escalas = detalle_escalas
        self.version = version
        self.idiomas_disponibles = idiomas_disponibles
        self.fecha_actualizacion = fecha_actualizacion