# Clase Producto representa un ítem del menú del restaurante.
# Contiene nombre, precio y categoría (bebida, plato fuerte, postre, etc.)

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        """Devuelve una cadena con la información del producto."""
        return f"{self.nombre} - ${self.precio} ({self.categoria})"
