from .proveedor_model import ProveedorModel

class ProveedorController:

    @staticmethod
    def obtener_proveedores():
        return ProveedorModel.obtener_proveedores()

    @staticmethod
    def obtener_proveedor(id: int):
        return ProveedorModel(id=id).obtener_proveedor()

    @staticmethod
    def crear_proveedor(data: dict):
        proveedor = ProveedorModel(
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"]
        )
        return proveedor.crear_proveedor()

    @staticmethod
    def modificar_proveedor(data: dict):
        proveedor = ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"]
        )
        return proveedor.modificar_proveedor()

    @staticmethod
    def eliminar_proveedor(id: int):
        proveedor = ProveedorModel(id=id)
        return proveedor.eliminar_proveedor()
