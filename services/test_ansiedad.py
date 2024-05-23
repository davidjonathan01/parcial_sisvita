from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.test_ansiedad import Test_Ansiedad
from schemas.test_ansiedad_schema import test_ansiedad_schema, tests_ansiedad_schema

test_ansiedad_routes = Blueprint("test_ansiedad_routes", __name__)

@test_ansiedad_routes.route('/test_ansiedad', methods=['POST'])
def create_test_ansiedad():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    n_preguntas = request.json.get('n_preguntas')
    detalle_escalas = request.json.get('detalle_escalas')
    version = request.json.get('version')
    idiomas_disponibles = request.json.get('idiomas_disponibles')
    fecha_actualizacion = request.json.get('fecha_actualizacion')

    new_test_ansiedad = Test_Ansiedad(
        nombre=nombre,
        descripcion=descripcion,
        n_preguntas=n_preguntas,
        detalle_escalas=detalle_escalas,
        version=version,
        idiomas_disponibles=idiomas_disponibles,
        fecha_actualizacion=fecha_actualizacion
    )

    db.session.add(new_test_ansiedad)
    db.session.commit()

    result = test_ansiedad_schema.dump(new_test_ansiedad)

    data = {
        'message': 'Nuevo test de ansiedad creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@test_ansiedad_routes.route('/test_ansiedad', methods=['GET'])
def get_tests_ansiedad():
    all_tests_ansiedad = Test_Ansiedad.query.all()
    result = tests_ansiedad_schema.dump(all_tests_ansiedad)

    data = {
        'message': 'Todos los tests de ansiedad han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_ansiedad_routes.route('/test_ansiedad/<int:id>', methods=['GET'])
def get_test_ansiedad(id):
    test_ansiedad = Test_Ansiedad.query.get(id)

    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = test_ansiedad_schema.dump(test_ansiedad)

    data = {
        'message': 'Test de ansiedad encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_ansiedad_routes.route('/test_ansiedad/<int:id>', methods=['PUT'])
def update_test_ansiedad(id):
    test_ansiedad = Test_Ansiedad.query.get(id)

    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    n_preguntas = request.json.get('n_preguntas')
    detalle_escalas = request.json.get('detalle_escalas')
    version = request.json.get('version')
    idiomas_disponibles = request.json.get('idiomas_disponibles')
    fecha_actualizacion = request.json.get('fecha_actualizacion')

    test_ansiedad.nombre = nombre
    test_ansiedad.descripcion = descripcion
    test_ansiedad.n_preguntas = n_preguntas
    test_ansiedad.detalle_escalas = detalle_escalas
    test_ansiedad.version = version
    test_ansiedad.idiomas_disponibles = idiomas_disponibles
    test_ansiedad.fecha_actualizacion = fecha_actualizacion

    db.session.commit()

    result = test_ansiedad_schema.dump(test_ansiedad)

    data = {
        'message': 'Test de ansiedad actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@test_ansiedad_routes.route('/test_ansiedad/<int:id>', methods=['DELETE'])
def delete_test_ansiedad(id):
    test_ansiedad = Test_Ansiedad.query.get(id)

    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(test_ansiedad)
    db.session.commit()

    data = {
        'message': 'Test de ansiedad eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
