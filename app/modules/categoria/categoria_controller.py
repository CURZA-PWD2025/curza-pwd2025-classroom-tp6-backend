from .categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def obtener_categorias():
        return CategoriaModel.obtener_categorias()

    @staticmethod
    def obtener_categoria(id: int):
        return CategoriaModel(id=id).obtener_categoria()

    @staticmethod
    def crear_categoria(data: dict):
        categoria = CategoriaModel(nombre=data["nombre"])
        return categoria.crear_categoria()

    @staticmethod
    def modificar_categoria(data: dict):
        categoria = CategoriaModel(id=data["id"], nombre=data["nombre"])
        return categoria.modificar_categoria()

    @staticmethod
    def eliminar_categoria(id: int):
        categoria = CategoriaModel(id=id)
        return categoria.eliminar_categoria()
