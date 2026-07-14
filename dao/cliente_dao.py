from config.conexcion import Conexion
from modelo.cliente import Cliente


class ClienteDAO:
    """Clase encargada de las operaciones CRUD en la base de datos"""

    def __init__(self):
        # ✅ Guardamos la instancia completa de Conexion (no se destruye)
        self.gestor_conexion = Conexion()
        self.conexion = self.gestor_conexion.obtener_conexion()

    # ==========================================
    # CREATE (INSERTAR)
    # ==========================================
    def insertar_cliente(self, cliente):
        """Inserta un nuevo cliente y retorna el ID generado"""
        cursor = self.conexion.cursor()
        sql = """
            INSERT INTO Clientes (Nombres, Telefono, Correo) 
            OUTPUT INSERTED.IdCliente 
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (cliente.nombres, cliente.telefono, cliente.correo))
        id_generado = cursor.fetchone()[0]
        self.conexion.commit()
        return id_generado

    # ==========================================
    # READ ALL (LISTAR)
    # ==========================================
    def seleccionar_todos(self):
        """Retorna todos los clientes de la base de datos"""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT IdCliente, Nombres, Telefono, Correo FROM Clientes ORDER BY IdCliente")
        registros = cursor.fetchall()

        clientes = []
        for row in registros:
            cliente = Cliente(
                id_cliente=row.IdCliente,
                nombres=row.Nombres,
                telefono=row.Telefono,
                correo=row.Correo
            )
            clientes.append(cliente)
        return clientes

    # ==========================================
    # READ ONE (BUSCAR)
    # ==========================================
    def seleccionar_por_id(self, id_cliente):
        """Busca un cliente por su ID"""
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT IdCliente, Nombres, Telefono, Correo FROM Clientes WHERE IdCliente = ?",
            (id_cliente,)
        )
        registro = cursor.fetchone()

        if registro:
            return Cliente(
                id_cliente=registro.IdCliente,
                nombres=registro.Nombres,
                telefono=registro.Telefono,
                correo=registro.Correo
            )
        return None

    # ==========================================
    # UPDATE (EDITAR)
    # ==========================================
    def actualizar_cliente(self, id_cliente, cliente):
        """Actualiza los datos de un cliente existente"""
        cursor = self.conexion.cursor()
        sql = "UPDATE Clientes SET Nombres = ?, Telefono = ?, Correo = ? WHERE IdCliente = ?"
        cursor.execute(sql, (cliente.nombres, cliente.telefono, cliente.correo, id_cliente))
        self.conexion.commit()
        return cursor.rowcount > 0

    # ==========================================
    # DELETE (ELIMINAR)
    # ==========================================
    def eliminar_cliente(self, id_cliente):
        """Elimina un cliente por su ID"""
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM Clientes WHERE IdCliente = ?", (id_cliente,))
        self.conexion.commit()
        return cursor.rowcount > 0