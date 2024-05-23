from datetime import datetime

from utils.db import db
from models.expp_estudiante import ExpP_Estudiante
from models.eval_ansiedad import Eval_Ansiedad

class Hist_Ev_Ansiedad(db.Model):
    __tablename__ = 'hist_ev_ansiedad'

    id_eval_ansiedad = db.Column(db.Integer, db.ForeignKey('eval_ansiedad.id_eval_ansiedad'), primary_key=True)
    id_exp_psicologico = db.Column(db.Integer, db.ForeignKey('expp_estudiante.id_exp_psicologico'), primary_key=True)
    fecha_actualizacion = db.Column(db.Date, nullable=False)

    eval_ansiedad = db.relationship('Eval_Ansiedad', backref='hist_ev_ansiedad')
    exp_psicologico = db.relationship('ExpP_Estudiante', backref='hist_ev_ansiedad')

    def __init__(self, id_eval_ansiedad, id_exp_psicologico, fecha_actualizacion=datetime.now()):
        self.id_eval_ansiedad = id_eval_ansiedad
        self.id_exp_psicologico = id_exp_psicologico
        self.fecha_actualizacion = fecha_actualizacion