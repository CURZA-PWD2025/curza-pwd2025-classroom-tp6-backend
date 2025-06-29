from .marca_model import MarcaModel

class MarcaController:

    @staticmethod
    def obtener_marcas():
        return MarcaModel.obtener_marcas()

    @staticmethod
    def obtener_marca(id: int):
        return MarcaModel(id=id).obtener_marca()

    @staticmethod
    def crear_marca(data: dict):
        marca = MarcaModel(nombre=data["nombre"])
        return marca.crear_marca()

    @staticmethod
    def modificar_marca(data: dict):
        marca = MarcaModel(id=data["id"], nombre=data["nombre"])
        return marca.modificar_marca()

    @staticmethod
    def eliminar_marca(id: int):
        marca = MarcaModel(id=id)
        return marca.eliminar_marca()
