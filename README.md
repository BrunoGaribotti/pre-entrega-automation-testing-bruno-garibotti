# Pre-entrega Automation Testing

Propósito del proyecto

Este proyecto automatiza pruebas de interfaz sobre la página web saucedemo.com. En principio, realiza sólo tres pruebas:

1ero test_01_login.py: prueba iniciar sesión con credenciales determinadas.
2do test_02_inventory.py: prueba que estemos efectivamente en la página de inventario, y que se muestren productos. Además, nos indica el nombre y precio del primer producto encontrado.
3ero test_03_cart.py: prueba agregar un producto al carrito, que efectivamente cambie la numeración del carrito, y que se navegue correctamente por el carrito (chequeando en el mismo que se haya agregado correctamente el producto).

Cada test abre su propio navegador y hace su propio login, así que puede ejecutarse de forma independiente.

# Tecnologías utilizadas
Python: lenguaje de programación
Selenium WebDriver: automatización del navegador (Google Chrome)
Pytest: framework de testing
pytest-html: generación del reporte HTML
Git y GitHub: control de versiones

# Estructura del proyecto

| Archivo | Test | Qué valida |
|---|---|---|
| `test_login.py` | `test_login_exitoso` | Login con `standard_user`: redirección a `/inventory.html` y visibilidad del logo "Swag Labs" y del título "Products" |
| `test_inventory.py` | `test_inventory` | Título de la página, presencia de productos, nombre y precio del primer producto, y visibilidad del menú y del filtro |
| `test_cart.py` | `test_agregar_producto_al_carrito` | Agregar el primer producto al carrito, que el contador pase a 1 y que el producto aparezca en el carrito |


# Instalación de dependencias

1. Clonar el repositorio.
2. Tener instalado Python y Google Chrome.
3. Instalar las dependencias (pip install -r requirements.txt)
4. Para ejecutar las pruebas, se utiliza pytest -v