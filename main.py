# Archivo principal del sistema.
# Aquí se ejecuta el programa utilizando las clases importadas.

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def main():
    # Crear restaurante
    restaurante = Restaurante("La Buena Mesa")

    # Crear productos del menú
    p1 = Producto("Hamburguesa", 8.50, "Plato fuerte")
    p2 = Producto("Batido de mora", 1.50, "Bebida")
    p3 = Producto("Pastel de chocolate", 2.00, "Postre")

    # Agregar productos al menú
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(p3)

    # Mostrar menú
    print("=== MENÚ DEL RESTAURANTE ===")
    for item in restaurante.mostrar_menu():
        print(item)

    # Registrar cliente
    cliente = Cliente("Alfredo")
    restaurante.registrar_cliente(cliente)

    # Cliente realiza pedidos
    cliente.agregar_pedido(p1)
    cliente.agregar_pedido(p2)

    # Muestra pedidos del cliente
    print("\n=== PEDIDOS DE ALFREDO ===")
    for pedido in cliente.mostrar_pedidos():
        print(pedido)

    # Total a pagar
    print(f"\nTotal a pagar: ${cliente.calcular_total()}")

if __name__ == "__main__":
    main()
