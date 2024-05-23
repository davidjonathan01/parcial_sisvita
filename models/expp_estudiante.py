from datetime import datetime

from utils.db import db
from models.estudiante import Estudiante

class ExpP_Estudiante(db.Model):
    __tablename__ = 'expp_estudiante'

    id_exp_psicologico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    estado_salud_mental = db.Column(db.String(30), nullable=False)
    fecha_actualizacion = db.Column(db.Date, nullable=False)

    estudiante = db.relationship('Estudiante', backref='expp_estudiante')

    def __init__(self, id_estudiante, anio, estado_salud_mental, fecha_actualizacion=datetime.now()):
        self.id_estudiante = id_estudiante
        self.anio = anio
        self.estado_salud_mental = estado_salud_mental
        self.fecha_actualizacion = fecha_actualizacion