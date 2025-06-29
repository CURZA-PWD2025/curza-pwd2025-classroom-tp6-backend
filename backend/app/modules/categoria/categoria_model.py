from ...database.connect_db import ConnectDB

class CategoriaModel:
    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data: dict):
        return CategoriaModel(id=data["id"], nombre=data["nombre"])

    @staticmethod
    def obtener_categorias():
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS")
                categorias = cursor.fetchall()
                return categorias if categorias else []
        except Exception as ex:
            return {"message": f"No se pudieron obtener categorías: {ex}"}
        finally:
            if conn:
                conn.close()

    def obtener_categoria(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                categoria = cursor.fetchone()
                return categoria if categoria else {"message": "Categoría no encontrada"}
        except Exception as ex:
            return {"message": f"Error al obtener la categoría: {ex}"}
        finally:
            if conn:
                conn.close()

    def crear_categoria(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("INSERT INTO CATEGORIAS (nombre) VALUES (%s)", (self.nombre,))
                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (id,))
                categoria = cursor.fetchone()
                return categoria if categoria else {"message": "No se pudo obtener la categoría creada"}
        except Exception as ex:
            return {"message": f"No se pudo crear la categoría: {ex}"}
        finally:
            if conn:
                conn.close()

    def modificar_categoria(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE CATEGORIAS SET nombre=%s WHERE id=%s",
                    (self.nombre, self.id)
                )
                conn.commit()
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                categoria = cursor.fetchone()
                return categoria if categoria else {"message": "No se pudo obtener la categoría actualizada"}
        except Exception as ex:
            return {"message": f"Error al modificar la categoría: {ex}"}
        finally:
            if conn:
                conn.close()

    def eliminar_categoria(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                categoria = cursor.fetchone()
                cursor.execute("DELETE FROM CATEGORIAS WHERE id=%s", (self.id,))
                conn.commit()
                if categoria:
                    return {"message": f"Categoría eliminada correctamente", "categoria": categoria}
                return {"message": "La categoría no existía"}
        except Exception as ex:
            return {"message": f"Error al eliminar la categoría: {ex}"}
        finally:
            if conn:
                conn.close()
