from selenium import webdriver
from selenium.webdriver.common.by import By

# Importar la función de login para no repetir código
from utils.helpers import login

def test_inventory():
    driver = webdriver.Chrome()

    try:
        # Login
        login(driver)

        # Verificar que la URL actual sea la página de inventario
        assert "/inventory.html" in driver.current_url

        # Verificar que el logo de la aplicación esté presente en la página de inventario
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # Verificar que estemos en la sección "Products"
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

        # Comienza test de inventario
        # Verificar que el título de la página sea "Swag Labs"
        assert driver.title == "Swag Labs"

        # Verificar que haya productos en la página de inventario
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        hay_productos = len(productos) > 0
        print(f"\nCantidad de productos: {len(productos)}")

        nombre_producto = (
            productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        )
        precio_producto = (
            productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        )
        # Verificar que el 1er producto tenga nombre y precio
        assert nombre_producto != ""
        assert precio_producto != ""
        print(f"Nombre del primer producto: {nombre_producto}")
        print(f"Precio del primer producto: {precio_producto}")

        # Verificar que es visible el filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

        # Verificar que es visible botón de el menú
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

    finally:
        # Cerrar el navegador
        driver.quit()
