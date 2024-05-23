from utils.db import db
from models.test_ansiedad import Test_Ansiedad
class Eval_Ansiedad(db.Model):
    __tablename__ = 'eval_ansiedad'

    id_eval_ansiedad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test_ansiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.id_test_ansiedad'), nullable=False)
    respuestas_formulario = db.Column(db.String(300), nullable=False)
    fecha_evaluacion = db.Column(db.Date, nullable=False)

    test_ansiedad = db.relationship('Test_Ansiedad', backref='eval_ansiedad')
    
    # constructor de la clase
    def __init__(self, id_test_ansiedad, respuestas_formulario, fecha_evaluacion):
        self.id_test_ansiedad = id_test_ansiedad
        self.respuestas_formulario = respuestas_formulario
        self.fecha_evaluacion = fecha_evaluacion