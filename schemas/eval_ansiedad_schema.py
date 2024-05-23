from utils.ma import ma
from models.eval_ansiedad import Eval_Ansiedad
from marshmallow import fields
from schemas.test_ansiedad_schema import Test_Ansiedad_Schema

class Eval_Ansiedad_Schema(ma.Schema):
    class Meta:
        model=Eval_Ansiedad
        fields=('id_eval_ansiedad',
               'id_test_ansiedad',
               'respuestas_formulario',
               'fecha_evaluacion',
               'test_ansiedad'
               )
    test_ansiedad=ma.Nested(Test_Ansiedad_Schema)  
eval_ansiedad_schema = Eval_Ansiedad_Schema()
evals_ansiedad_schema = Eval_Ansiedad_Schema(many=True)