class Producto:
    def __init__(self, descripcion, cantidad):
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __str__(self):
        cadena = self.descripcion + " – " + self.cantidad
        return cadena
 