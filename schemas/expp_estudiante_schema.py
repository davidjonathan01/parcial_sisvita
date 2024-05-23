from utils.ma import ma
from models.expp_estudiante import ExpP_Estudiante
from marshmallow import fields
from schemas.estudiante_schema import Estudiante_Schema

class ExpP_Estudiante_Schema(ma.Schema):
    class Meta:
        model=ExpP_Estudiante
        fields=('id_exp_psicologico',
               'id_estudiante',
               'anio',
               'estado_salud_mental',
               'fecha_actualizacion',
               'estudiante')
        
    estudiante=ma.Nested(Estudiante_Schema)    
exp_psi_estudiante_schema = ExpP_Estudiante_Schema()
exps_psi_estudiante_schema = ExpP_Estudiante_Schema(many=True)