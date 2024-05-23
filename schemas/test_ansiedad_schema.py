from utils.ma import ma
from models.test_ansiedad import Test_Ansiedad
from marshmallow import fields

class Test_Ansiedad_Schema(ma.Schema):
    class Meta:
        model=Test_Ansiedad
        fields=('id_test_ansiedad',
               'nombre',
               'descripcion',
               'n_preguntas',
               'detalle_escalas',
               'version',
               'idiomas_disponibles',
               'fecha_actualizacion')

test_ansiedad_schema = Test_Ansiedad_Schema()
tests_ansiedad_schema = Test_Ansiedad_Schema(many=True)