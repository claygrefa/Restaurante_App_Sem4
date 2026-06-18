# Clase Cliente representa a un cliente del restaurante.
# Contiene nombre y una lista de productos que ha pedido.

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []  # Lista de productos

    def agregar_pedido(self, producto):
        """Agrega un producto al pedido del cliente."""
        self.pedidos.append(producto)

    def calcular_total(self):
        """Calcula el total a pagar sumando los precios de los productos."""
        return sum(p.precio for p in self.pedidos)

    def mostrar_pedidos(self):
        """Devuelve una lista con la información de cada producto pedido."""
        return [p.mostrar_info() for p in self.pedidos]
