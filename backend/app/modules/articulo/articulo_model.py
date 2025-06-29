from ...database.connect_db import ConnectDB
from app.modules.marca.marca_model import MarcaModel as Marca
from app.modules.proveedor.proveedor_model import ProveedorModel as Proveedor
from app.modules.categoria.categoria_model import CategoriaModel as Categoria

class ArticuloModel:
    def __init__(self, id=0, descripcion="", precio=0.0, stock=0, marca=None, proveedor=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias or []

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar() if self.marca else None,
            "proveedor": self.proveedor.serializar() if self.proveedor else None,
            "categorias": self.categorias,
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            marca=data["marca"],
            proveedor=data["proveedor"],
            categorias=data["categorias"],
        )

    @staticmethod
    def obtener_articulos():
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS")
                articulos = []
                arts = cursor.fetchall()

                for articulo in arts:
                    cursor.execute("SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (articulo["id"],))
                    categorias = [Categoria(cat["categoria_id"]).obtener_categoria() for cat in cursor.fetchall()]
                    articulo["categorias"] = categorias

                    articulo["marca"] = Marca(articulo["marca_id"]).obtener_marca()
                    articulo["proveedor"] = Proveedor(articulo["proveedor_id"]).obtener_proveedor()
                    del articulo["marca_id"]
                    del articulo["proveedor_id"]

                    articulos.append(articulo)

                return articulos if articulos else []
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def obtener_articulo(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (self.id,))
                articulo = cursor.fetchone()
                if not articulo:
                    return {"message": "Artículo no encontrado"}

                cursor.execute("SELECT * FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s", (self.id,))
                categorias = [Categoria(cat["categoria_id"]).obtener_categoria() for cat in cursor.fetchall()]

                articulo["marca"] = Marca(articulo["marca_id"]).obtener_marca()
                articulo["proveedor"] = Proveedor(articulo["proveedor_id"]).obtener_proveedor()
                del articulo["marca_id"]
                del articulo["proveedor_id"]
                articulo["categorias"] = categorias

                return articulo
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def crear_articulo(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
                    (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id)
                )
                conn.commit()
                articulo_id = cursor.lastrowid

                for categoria in self.categorias:
                    cursor.execute(
                        "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                        (articulo_id, categoria)
                    )
                conn.commit()

                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (articulo_id,))
                return cursor.fetchone() or {"message": "Artículo no creado"}
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def modificar_articulo(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE ARTICULOS SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s",
                    (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id, self.id)
                )
                cursor.execute(
                    "DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s", (self.id,)
                )
                for categoria in self.categorias:
                    cursor.execute(
                        "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                        (self.id, categoria)
                    )
                conn.commit()

                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (self.id,))
                return cursor.fetchone() or {"message": "No se pudo obtener el artículo actualizado"}
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def eliminar_articulo(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s", (self.id,))
                cursor.execute("DELETE FROM ARTICULOS WHERE id=%s", (self.id,))
                conn.commit()
                return {"message": "Se ha eliminado el artículo"}
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()
