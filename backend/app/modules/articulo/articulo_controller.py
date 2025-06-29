from .articulo_model import ArticuloModel
from ..marca.marca_model import MarcaModel as Marca
from ..proveedor.proveedor_model import ProveedorModel as Proveedor
from ..categoria.categoria_model import CategoriaModel as Categoria


class ArticuloController:

    @staticmethod
    def obtener_articulos():
        return ArticuloModel.obtener_articulos()

    @staticmethod
    def obtener_articulo(id: int):
        return ArticuloModel(id=id).obtener_articulo()

    @staticmethod
    def crear_articulo(data: dict):
        mark = Marca(id=data["marca_id"]).obtener_marca()
        prov = Proveedor(id=data["proveedor_id"]).obtener_proveedor()

        if not mark or not prov:
            return {"message": "Marca o proveedor no encontrados"}

        marca = Marca.deserializar(mark)
        proveedor = Proveedor.deserializar(prov)
        categorias = data["categorias"]

        articulo = ArticuloModel(
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            marca=marca,
            proveedor=proveedor,
            categorias=categorias,
        )
        return articulo.crear_articulo()

    @staticmethod
    def modificar_articulo(data: dict):
        mark = Marca(id=data["marca_id"]).obtener_marca()
        prov = Proveedor(id=data["proveedor_id"]).obtener_proveedor()

        if not mark or not prov:
            return {"message": "Marca o proveedor no encontrados"}

        marca = Marca.deserializar(mark)
        proveedor = Proveedor.deserializar(prov)
        categorias = data["categorias"]

        articulo = ArticuloModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            marca=marca,
            proveedor=proveedor,
            categorias=categorias,
        )
        return articulo.modificar_articulo()

    @staticmethod
    def eliminar_articulo(id: int):
        articulo = ArticuloModel(id=id)
        return articulo.eliminar_articulo()
