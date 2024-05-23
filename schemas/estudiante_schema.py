from utils.ma import ma
from models.estudiante import Estudiante
from marshmallow import fields

class Estudiante_Schema(ma.Schema):
    class Meta:
        model=Estudiante
        fields = ('id_estudiante',
              'doc_identificacion',
              'nombres',
              'apellidos',
              'fecha_nacimiento',
              'correo_electronico',
              'genero',
              'direccion',
              'numero_telefono',
              'carrera_universitaria',
              'año_ingreso'
              )
estudiante_schema = Estudiante_Schema()
estudiantes_schema = Estudiante_Schema(many=True)
