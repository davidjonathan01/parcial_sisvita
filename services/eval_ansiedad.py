# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.eval_ansiedad import Eval_Ansiedad
from schemas.eval_ansiedad_schema import eval_ansiedad_schema, evals_ansiedad_schema

eval_ansiedad_routes = Blueprint("eval_ansiedad_routes", __name__)

@eval_ansiedad_routes.route('/eval_ansiedad', methods=['POST'])
def create_eval_ansiedad():
    id_test_ansiedad = request.json.get('id_test_ansiedad')
    respuestas_formulario = request.json.get('respuestas_formulario')
    fecha_evaluacion = request.json.get('fecha_evaluacion')

    new_eval_ansiedad = Eval_Ansiedad(id_test_ansiedad=id_test_ansiedad, respuestas_formulario=respuestas_formulario, fecha_evaluacion=fecha_evaluacion)

    db.session.add(new_eval_ansiedad)
    db.session.commit()

    result = eval_ansiedad_schema.dump(new_eval_ansiedad)

    data = {
        'message': 'Nuevo registro de evaluación de ansiedad creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@eval_ansiedad_routes.route('/eval_ansiedad', methods=['GET'])
def get_all_evaluaciones_ansiedad():
    all_evaluaciones_ansiedad = Eval_Ansiedad.query.all()
    result = evals_ansiedad_schema.dump(all_evaluaciones_ansiedad)
    
    data = {
        'message': 'Todas las evaluaciones de ansiedad han sido encontradas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['GET'])
def get_eval_ansiedad(id):
    eval_ansiedad = Eval_Ansiedad.query.get(id)
    if eval_ansiedad:
        result = eval_ansiedad_schema.dump(eval_ansiedad)
        data = {
            'message': 'Evaluación de ansiedad encontrada',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    else:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['PUT'])
def update_eval_ansiedad(id):
    eval_ansiedad = Eval_Ansiedad.query.get(id)
    if not eval_ansiedad:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    id_test_ansiedad = request.json.get('id_test_ansiedad')
    respuestas_formulario = request.json.get('respuestas_formulario')
    fecha_evaluacion = request.json.get('fecha_evaluacion')
    
    eval_ansiedad.id_test_ansiedad = id_test_ansiedad
    eval_ansiedad.respuestas_formulario = respuestas_formulario
    eval_ansiedad.fecha_evaluacion = fecha_evaluacion
    
    db.session.commit()
    
    result = eval_ansiedad_schema.dump(eval_ansiedad)
    data = {
        'message': 'Evaluación de ansiedad actualizada',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['DELETE'])
def delete_eval_ansiedad(id):
    eval_ansiedad = Eval_Ansiedad.query.get(id)

    if not eval_ansiedad:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(eval_ansiedad)
    db.session.commit()

    data = {
        'message': 'Evaluación de ansiedad eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)