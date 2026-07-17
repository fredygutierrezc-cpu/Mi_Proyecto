# Paquete de configuración
# Este archivo hace que la carpeta 'config' sea reconocida como un paquete de Python
# Contiene la configuracion de la base de datos 

from config.conexcion import Conexion

__all__ = ['Conexion']
