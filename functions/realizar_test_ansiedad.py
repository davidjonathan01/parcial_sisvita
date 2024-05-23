from flask import Blueprint, jsonify, make_response, request
from models.estudiante import Estudiante
from models.test_ansiedad import Test_Ansiedad
from models.eval_ansiedad import Eval_Ansiedad
from models.hist_ev_ansiedad import Hist_Ev_Ansiedad
from models.expp_estudiante import ExpP_Estudiante
from schemas.eval_ansiedad_schema import Eval_Ansiedad_Schema
from schemas.hist_ev_ansiedad_schema import Hist_Ev_Ansiedad_Schema
from schemas.expp_estudiante_schema import ExpP_Estudiante_Schema

from datetime import datetime
from utils.db import db

cus = Blueprint('cus', __name__)

@cus.route('/realizar_test_ansiedad/<int:id_estudiante>/<int:id_test_ansiedad>', methods=['POST'])
def realizar_test_ansiedad(id_estudiante, id_test_ansiedad):
    # Buscar al estudiante
    estudiante = Estudiante.query.get(id_estudiante)
    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Buscar el test de ansiedad que se va a realizar
    test_ansiedad = Test_Ansiedad.query.get(id_test_ansiedad)
    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Mostrar las preguntas del test de ansiedad
    if test_ansiedad.id_test_ansiedad == 1:
        preguntas = "mostrar link de preguntas del test de ansiedad 1"
    elif test_ansiedad.id_test_ansiedad == 2:
        preguntas = "mostrar link de preguntas del test de ansiedad 2"
    elif test_ansiedad.id_test_ansiedad == 3:
        preguntas = "mostrar link de preguntas del test de ansiedad 3"

    # Registrar las respuestas del estudiante
    respuestas = request.json.get('respuestas')

    # Guardar las respuestas en la base de datos
    new_eval_ansiedad = Eval_Ansiedad(
        id_test_ansiedad=id_test_ansiedad,
        respuestas_formulario=respuestas,
        fecha_evaluacion=datetime.now()
    )

    db.session.add(new_eval_ansiedad)
    db.session.commit()

    eval_ansiedad_schema = Eval_Ansiedad_Schema()
    result1 = eval_ansiedad_schema.dump(new_eval_ansiedad)

    # Buscar el expediente psicológico del estudiante
    exp_psicologico = ExpP_Estudiante.query.filter_by(id_estudiante=id_estudiante).first()

    if not exp_psicologico:
        id_estudiante = estudiante.id_estudiante
        anio = datetime.now().year
        estado_salud_mental = 'Saludable'
        fecha_actualizacion = datetime.now()

        new_exp_psicologico = ExpP_Estudiante(
            id_estudiante=id_estudiante,
            anio=anio,
            estado_salud_mental=estado_salud_mental,
            fecha_actualizacion=fecha_actualizacion
        )

        db.session.add(new_exp_psicologico)
        db.session.commit()

        expp_estudiante_schema = ExpP_Estudiante_Schema()
        result3 = expp_estudiante_schema.dump(exp_psicologico)
    else:
        result3 = None

    if exp_psicologico is not None:
        new_hist_ev_ansiedad = Hist_Ev_Ansiedad(
            id_eval_ansiedad=new_eval_ansiedad.id_eval_ansiedad,
            id_exp_psicologico=exp_psicologico.id_exp_psicologico,
            fecha_actualizacion=datetime.now()
        )
        result3 = "NO SE CREO EXPEDIENTE PSICOLOGICO"
    else:
        id_estudiante = estudiante.id_estudiante
        anio = datetime.now().year
        estado_salud_mental = 'Saludable'
        fecha_actualizacion = datetime.now()

        new_exp_psicologico = ExpP_Estudiante(
            id_estudiante=id_estudiante,
            anio=anio,
            estado_salud_mental=estado_salud_mental,
            fecha_actualizacion=fecha_actualizacion
        )

        db.session.add(new_exp_psicologico)
        db.session.commit()

        expp_estudiante_schema = ExpP_Estudiante_Schema()
        result3 = expp_estudiante_schema.dump(new_exp_psicologico)

    db.session.add(new_hist_ev_ansiedad)
    db.session.commit()

    hist_ev_ansiedad_schema = Hist_Ev_Ansiedad_Schema()
    result2 = hist_ev_ansiedad_schema.dump(new_hist_ev_ansiedad)

    data = {
        'message': 'Test de ansiedad realizado exitosamente',
        'status': 201,
        'respuestas': result1,
        'historial_evaluaciones': result2,
        'expediente_psicologico': result3
    }

    return make_response(jsonify(data), 201)