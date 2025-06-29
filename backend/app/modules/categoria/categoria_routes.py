from .categoria_controller import CategoriaController
from flask import Blueprint, jsonify, request

categoria_bp = Blueprint("categoria", __name__)

@categoria_bp.route("/", methods=["GET"])
def obtener_categorias():
    try:
        categorias = CategoriaController.obtener_categorias()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({"message": "No se encontraron categorías"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@categoria_bp.route("/<int:id>", methods=["GET"])
def obtener_categoria(id):
    try:
        categoria = CategoriaController.obtener_categoria(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"message": "No se encontró la categoría"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@categoria_bp.route("/", methods=["POST"])
def crear_categoria():
    try:
        data = request.get_json()
        result = CategoriaController.crear_categoria(data)
        return jsonify(result), 201
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@categoria_bp.route("/<int:id>", methods=["PUT"])
def modificar_categoria(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = CategoriaController.modificar_categoria(data)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró la categoría con id {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500

@categoria_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    try:
        result = CategoriaController.eliminar_categoria(id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró la categoría con id {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500
