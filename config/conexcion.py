import sqlite3
import os

class Conexion:
    #Clase encargada de gestionar la conexión a SQLite
    
    # Ruta del archivo de base de datos (se crea automáticamente)
    RUTA_BD = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
        "bd_restaurante.db"
    )
    
    @staticmethod
    def obtener_conexion():
        #Retorna una conexión activa a la base de datos SQLite
        try:
            conexion = sqlite3.connect(Conexion.RUTA_BD)
            conexion.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
            return conexion
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
        #Muestra mensajes d error si falla la conxcion y devuelve nulo
            return None
    
    @staticmethod
    def cerrar_conexion(conexion):
        #Cierra la conexión de forma segura
        if conexion:
            conexion.close()
    
    @staticmethod
    def crear_tablas(conexion):
        #Crea las tablas si no existen
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Clientes (
                    IdCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombres VARCHAR(100) NOT NULL,
                    Telefono VARCHAR(9) NULL,
                    Correo VARCHAR(100) NULL
                )
            """)
            conexion.commit()
            print("[✓ INFO] Tablas verificadas/creadas correctamente.")
        except Exception as e:
            print(f"[ERROR] No se pudieron crear las tablas: {e}")
