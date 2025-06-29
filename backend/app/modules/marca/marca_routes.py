from .marca_controller import MarcaController
from flask import Blueprint, jsonify, request


marca_bp = Blueprint("marca", __name__)


@marca_bp.route("/", methods=["GET"])
def obtener_marcas():
    try:
        marcas = MarcaController.obtener_marcas()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({"message": "No se encontraron marcas"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@marca_bp.route("/<int:id>", methods=["GET"])
def obtener_marca(id):
    try:
        marca = MarcaController.obtener_marca(id)
        if marca:
            return jsonify(marca), 200
        else:
            return jsonify({"message": "No se encontró la marca"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@marca_bp.route("/", methods=["POST"])
def crear_marca():
    try:
        data = request.get_json()
        result = MarcaController.crear_marca(data)
        if result:
            return jsonify(result), 201
        else:
            return jsonify({"message": "No se pudo crear la marca"}), 400
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@marca_bp.route("/<int:id>", methods=["PUT"])
def modificar_marca(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = MarcaController.modificar_marca(data)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró la marca con id {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@marca_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_marca(id):
    try:
        result = MarcaController.eliminar_marca(id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró la marca con id {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500
