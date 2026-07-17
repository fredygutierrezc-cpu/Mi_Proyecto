#Importa la conecion con la base de datos 
from config.conexcion import Conexion
#Importa el modulo de la entidad cliente
from modelo.cliente import Cliente
#Importa librerias para manejar rutas del proyecto 
import sys
import os

# Agregar ruta raíz del proyecto
#asi se puede importar  los modulos sin eerrores  de ubicacion
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ClienteDAO:
    #Data Access Object para la tabla Clientes
    
    def __init__(self, conexion):
        self.conexion = conexion
    
    def insertar(self, cliente):
        #Inserta un nuevo cliente en la base de datos
        try:
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO Clientes (Nombres, Telefono, Correo) 
                VALUES (?, ?, ?)
            """
            cursor.execute(sql, (
                cliente.nombres,
                cliente.telefono,
                cliente.correo
            ))
            self.conexion.commit()
            return cursor.lastrowid  # Retorna el ID generado
        except Exception as e:
            print(f"[ERROR DAO] No se pudo insertar: {e}")
            return None
    
    def listar(self):
        #Lista todos los clientes
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT IdCliente, Nombres, Telefono, Correo FROM Clientes ORDER BY IdCliente")
            registros = cursor.fetchall()
            
            clientes = []
            for row in registros:
                cliente = Cliente(
                    id_cliente=row['IdCliente'],
                    nombres=row['Nombres'],
                    telefono=row['Telefono'],
                    correo=row['Correo']
                )
                clientes.append(cliente)
            
            return clientes
        except Exception as e:
            print(f"[ERROR DAO] No se pudo listar: {e}")
            return []
    
    def buscar_por_id(self, id_cliente):
        """Busca un cliente por su ID"""
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "SELECT IdCliente, Nombres, Telefono, Correo FROM Clientes WHERE IdCliente = ?",
                (id_cliente,)
            )
            row = cursor.fetchone()
            
            if row:
                return Cliente(
                    id_cliente=row['IdCliente'],
                    nombres=row['Nombres'],
                    telefono=row['Telefono'],
                    correo=row['Correo']
                )
            return None
        except Exception as e:
            print(f"[ERROR DAO] No se pudo buscar: {e}")
            return None
    
    def actualizar(self, cliente):
        #Actualiza un cliente existente
        try:
            cursor = self.conexion.cursor()
            sql = """
                UPDATE Clientes 
                SET Nombres = ?, Telefono = ?, Correo = ? 
                WHERE IdCliente = ?
            """
            cursor.execute(sql, (
                cliente.nombres,
                cliente.telefono,
                cliente.correo,
                cliente.id_cliente
            ))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[ERROR DAO] No se pudo actualizar: {e}")
            return False
    
    def eliminar(self, id_cliente):
        #Elimina un cliente por su ID 
        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM Clientes WHERE IdCliente = ?", (id_cliente,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[ERROR DAO] No se pudo eliminar: {e}")
            return False
