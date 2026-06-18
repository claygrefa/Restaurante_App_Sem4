# Clase Restaurante administra los productos disponibles y los pedidos de los clientes.

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []       # Lista de productos disponibles
        self.clientes = []   # Lista de clientes atendidos

    def agregar_producto(self, producto):
        """Agrega un producto al menú del restaurante."""
        self.menu.append(producto)

    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente en el restaurante."""
        self.clientes.append(cliente)

    def mostrar_menu(self):
        """Devuelve una lista con la información del menú."""
        return [p.mostrar_info() for p in self.menu]
