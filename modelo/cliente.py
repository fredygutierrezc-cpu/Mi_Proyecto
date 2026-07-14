class Cliente:
    """Clase entidad que representa un Cliente"""

    def __init__(self, id_cliente=None, nombres=None, telefono=None, correo=None):
        self.id_cliente = id_cliente
        self.nombres = nombres
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Cliente(ID={self.id_cliente}, Nombre={self.nombres})"

    def __repr__(self):
        return self.__str__()