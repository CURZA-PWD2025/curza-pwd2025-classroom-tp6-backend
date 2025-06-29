from ...database.connect_db import ConnectDB

class MarcaModel:
    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data: dict):
        return MarcaModel(id=data["id"], nombre=data["nombre"])

    @staticmethod
    def obtener_marcas():
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS")
                marcas = cursor.fetchall()
                return marcas if marcas else []
        except Exception as ex:
            return {"message": f"Error al obtener marcas: {ex}"}
        finally:
            if conn:
                conn.close()

    def obtener_marca(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                return marca if marca else {"message": "Marca no encontrada"}
        except Exception as ex:
            return {"message": f"Error al obtener la marca: {ex}"}
        finally:
            if conn:
                conn.close()

    def crear_marca(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%s)", (self.nombre,))
                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (id,))
                marca = cursor.fetchone()
                return marca if marca else {"message": "No se pudo obtener la marca creada"}
        except Exception as ex:
            return {"message": f"No se pudo crear la marca: {ex}"}
        finally:
            if conn:
                conn.close()

    def modificar_marca(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("UPDATE MARCAS SET nombre=%s WHERE id=%s", (self.nombre, self.id))
                conn.commit()
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                return marca if marca else {"message": "No se pudo obtener la marca actualizada"}
        except Exception as ex:
            return {"message": f"Error al modificar la marca: {ex}"}
        finally:
            if conn:
                conn.close()

    def eliminar_marca(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                cursor.execute("DELETE FROM MARCAS WHERE id=%s", (self.id,))
                conn.commit()
                if marca:
                    return {"message": "Marca eliminada correctamente", "marca": marca}
                return {"message": "La marca no existía"}
        except Exception as ex:
            return {"message": f"Error al eliminar la marca: {ex}"}
        finally:
            if conn:
                conn.close()
