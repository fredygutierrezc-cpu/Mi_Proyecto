import pyodbc


class Conexion:
    """Clase encargada de gestionar la conexión a la base de datos"""

    def __init__(self):
        self.conexion = self._conectar()
        if not self.conexion:
            raise ConnectionError("No se pudo establecer conexión con la base de datos.")

    def __del__(self):
        """Destructor: Cierra la conexión automáticamente"""
        if hasattr(self, 'conexion') and self.conexion:
            self.conexion.close()
            print("\n[INFO] Conexión a la base de datos cerrada correctamente.")

    def _conectar(self):
        """Método privado para establecer la conexión"""
        try:
            cadena = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=DESKTOP-GKH9TBM\\SQLEXPRESS;"
                "DATABASE=BD_Restaurante;"
                "Trusted_Connection=yes;"
            )
            return pyodbc.connect(cadena)
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def obtener_conexion(self):
        """Retorna la conexión activa"""
        return self.conexion