from .articulo_controller import ArticuloController
from flask import request, Blueprint, jsonify
from flask_cors import cross_origin

articulo_bp = Blueprint("articulo", __name__)

@articulo_bp.route("/", methods=["GET"])
@cross_origin()
def obtener_articulos():
    try:
        articulos = ArticuloController.obtener_articulos()
        return jsonify(articulos), 200
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@articulo_bp.route("/<int:id>", methods=["GET"])
@cross_origin()
def obtener_articulo(id):
    try:
        articulo = ArticuloController.obtener_articulo(id)
        return jsonify(articulo), 200
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@articulo_bp.route("/", methods=["POST"])
@cross_origin()
def crear_articulo():
    try:
        data = request.get_json()
        articulo = ArticuloController.crear_articulo(data)
        return jsonify(articulo), 201
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@articulo_bp.route("/<int:id>", methods=["PUT"])
@cross_origin()
def modificar_articulo(id):
    try:
        data = request.get_json()
        data["id"] = id
        articulo = ArticuloController.modificar_articulo(data=data)
        return jsonify(articulo), 200
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@articulo_bp.route("/<int:id>", methods=["DELETE"])
@cross_origin()
def eliminar_articulo(id):
    try:
        articulo = ArticuloController.eliminar_articulo(id)
        return jsonify(articulo), 200
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500
