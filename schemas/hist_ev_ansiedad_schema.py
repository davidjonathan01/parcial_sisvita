from utils.ma import ma
from models.hist_ev_ansiedad import Hist_Ev_Ansiedad
from marshmallow import fields
from schemas.expp_estudiante_schema import ExpP_Estudiante_Schema
from schemas.eval_ansiedad_schema import Eval_Ansiedad_Schema


class Hist_Ev_Ansiedad_Schema(ma.Schema):
    class Meta:
        model=Hist_Ev_Ansiedad
        fields=('id_eval_ansiedad',
                'id_exp_psicologico',
                'fecha_actualizacion',
                'eval_ansiedad',
                'exp_psicologico'
               )
    eval_ansiedad=ma.Nested(Eval_Ansiedad_Schema) 
    exp_psicologico=ma.Nested(ExpP_Estudiante_Schema)    

hist_eval_ansiedad_schema = Hist_Ev_Ansiedad_Schema()
hists_eval_ansiedad_schema = Hist_Ev_Ansiedad_Schema(many=True)