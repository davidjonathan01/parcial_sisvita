from utils.db import db
class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id_estudiante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doc_identificacion = db.Column(db.String(10), nullable=False, unique=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    correo_electronico = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    direccion = db.Column(db.String(500), nullable=False)
    numero_telefono = db.Column(db.String(20), nullable=False)
    carrera_universitaria = db.Column(db.String(50), nullable=False)
    anio_ingreso = db.Column(db.Integer, nullable=False)
    
    # constructor de la clase
    def __init__(self, doc_identificacion, nombres, apellidos, fecha_nacimiento, correo_electronico, genero, direccion, numero_telefono, carrera_universitaria, anio_ingreso):
        self.doc_identificacion = doc_identificacion
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.correo_electronico = correo_electronico
        self.genero = genero
        self.direccion = direccion
        self.numero_telefono = numero_telefono
        self.carrera_universitaria = carrera_universitaria
        self.anio_ingreso = anio_ingreso