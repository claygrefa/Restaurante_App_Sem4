# Sistema de Gestión de Restaurante - Programación Modular

Es una aplicación de consola en Python diseñada bajo el enfoque de la **Programación Orientada a Objetos (POO)** y la **arquitectura modular**. El sistema permite gestionar el menú de un restaurante, registrar clientes, tomar pedidos y calcular la factura correspondiente.

## 👤 Información del Estudiante
* **Nombre** Clay Medardo Grefa Tunay
* **Institución:** Universidad Estatal Amazónica
* **Materia:** Programación / Tecnología de la Información

---

## 📝 Descripción del Sistema
El sistema simula las operaciones cotidianas de un restaurante mediante una separación clara de funciones:
1. **Modelos de Datos:** Representación de entidades del mundo real (`Producto` y `Cliente`).
2. **Servicios de Lógica:** Control de flujos, gestión del menú, asignación de pedidos y procesamiento de cuentas finales.
3. **Punto de Control (`main.py`):** Ejecución coordinada de todos los componentes.

---

## 📂 Estructura del Proyecto y Modularización
El repositorio está organizado siguiendo estrictamente la separación de responsabilidades solicitada:

```text
restaurante_app/
│
├── modelos/               # Contiene las clases que definen los datos
│   ├── producto.py        # Clase Producto (id, nombre, precio)
│   └── cliente.py         # Clase Cliente (id, nombre, pedidos, cálculo individual)
│
├── servicios/             # Contiene la lógica del negocio
│   └── restaurante.py     # Clase RestauranteService (menú, lógica de orden y facturación)
│
├── main.py                # Orquestador principal del programa
└── README.md              # Documentación del proyecto
