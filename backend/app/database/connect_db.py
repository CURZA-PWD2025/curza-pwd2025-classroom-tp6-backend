import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectDB:
    
    @staticmethod
    def get_connect():
        try:
            conn = mysql.connector.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME'),
                host=os.getenv('DB_HOST', "localhost"),
                port=os.getenv('DB_PORT', 3306)
            )
            return conn
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    @staticmethod
    def read(sql: str, params: tuple = None):
        cxn = ConnectDB.get_connect()
        if not cxn:
            print("Failed to establish connection in 'read'")
            return None

        try:
            with cxn.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result if result else None
        except Exception as e:
            print(f"Error in READ query: {e}")
        finally:
            cxn.close()

    @staticmethod
    def write(sql: str, params: tuple = None):
        cxn = ConnectDB.get_connect()
        if not cxn:
            print("Failed to establish connection in 'write'")
            return None

        try:
            with cxn.cursor() as cursor:
                cursor.execute(sql, params)
                cxn.commit()
                return cursor.lastrowid
        except Exception as e:
            print(f"Error in WRITE query: {e}")
            cxn.rollback()
        finally:
            cxn.close()