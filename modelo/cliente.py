class Cliente:
    #Modelo/Entidad que representa un Cliente
    
    def __init__(self, id_cliente=None, nombres=None, telefono=None, correo=None):
        self._id_cliente = id_cliente
        self._nombres = nombres
        self._telefono = telefono
        self._correo = correo
    
    def __str__(self):
        return f"Cliente(ID={self.id_cliente}, Nombre={self.nombres}, Tel={self.telefono}, Correo={self.correo})"
