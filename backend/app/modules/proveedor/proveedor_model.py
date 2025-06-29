from ...database.connect_db import ConnectDB

class ProveedorModel:

    def __init__(self, id: int = 0, nombre: str = "", telefono: int = 0, direccion: str = "", email: str = ""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email,
        }

    @staticmethod
    def deserializar(data: dict):
        return ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"],
        )

    @staticmethod
    def obtener_proveedores():
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES")
                proveedores = cursor.fetchall()
                return proveedores if proveedores else []
        except Exception as ex:
            return {"message": f"No se encontraron proveedores: {ex}"}
        finally:
            if conn:
                conn.close()

    def obtener_proveedor(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                return proveedor if proveedor else False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def crear_proveedor(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO PROVEEDORES (nombre,telefono,direccion,email) VALUES (%s,%s,%s,%s)",
                    (self.nombre, self.telefono, self.direccion, self.email),
                )
                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (id,))
                proveedor = cursor.fetchone()
                return proveedor if proveedor else False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def modificar_proveedor(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE PROVEEDORES SET nombre=%s,telefono=%s,direccion=%s,email=%s WHERE id=%s",
                    (self.nombre, self.telefono, self.direccion, self.email, self.id),
                )
                conn.commit()
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                return proveedor if proveedor else False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()

    def eliminar_proveedor(self):
        conn = ConnectDB.get_connect()
        if not conn:
            return {"message": "No se pudo conectar con la base de datos"}

        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                cursor.execute("DELETE FROM PROVEEDORES WHERE id=%s", (self.id,))
                conn.commit()
                if proveedor:
                    return {"message": f"Proveedor eliminado correctamente: {proveedor}"}
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            if conn:
                conn.close()
