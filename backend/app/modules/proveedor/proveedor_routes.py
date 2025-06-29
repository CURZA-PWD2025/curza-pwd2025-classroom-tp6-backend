from .proveedor_controller import ProveedorController
from flask import Blueprint, jsonify, request

# Este blueprint se registrará como: app.register_blueprint(proveedor_bp, url_prefix="/proveedores")
proveedor_bp = Blueprint("proveedor", __name__)


@proveedor_bp.route("/", methods=["GET"])
def obtener_proveedores():
    try:
        proveedores = ProveedorController.obtener_proveedores()
        if proveedores:
            return jsonify(proveedores), 200
        else:
            return jsonify({"message": "No se encontraron proveedores"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@proveedor_bp.route("/<int:id>", methods=["GET"])
def obtener_proveedor(id):
    try:
        proveedor = ProveedorController.obtener_proveedor(id)
        if proveedor:
            return jsonify(proveedor), 200
        else:
            return jsonify({"message": "No se encontró el proveedor"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@proveedor_bp.route("/", methods=["POST"])
def crear_proveedor():
    try:
        data = request.get_json()
        result = ProveedorController.crear_proveedor(data)
        if result:
            return jsonify(result), 201
        else:
            return jsonify({"message": "No se pudo crear el proveedor"}), 400
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@proveedor_bp.route("/<int:id>", methods=["PUT"])
def modificar_proveedor(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = ProveedorController.modificar_proveedor(data)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró el proveedor con id: {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500


@proveedor_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_proveedor(id):
    try:
        result = ProveedorController.eliminar_proveedor(id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": f"No se encontró el proveedor con id: {id}"}), 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error: {ex}"}), 500
