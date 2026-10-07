from selenium import webdriver
from selenium.webdriver.common.by import By


def test_inventory():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        # Ingresar credenciales válidas y cliquear en el botón de Iniciar sesión
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        # Verificar que la URL actual sea la página de inventario
        assert "/inventory.html" in driver.current_url

        # Verificar que el logo de la aplicación esté presente en la página de inventario
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # Verificar que el titulo de la página sea "Products"
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

        # Comienza test de inventario
        # Verificar que el título de la página sea "Swag Labs"
        assert driver.title == "Swag Labs"

        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        hay_productos = len(productos) > 0
        print(f"\nCantidad de productos: {len(productos)}")

    finally:
        # Cerrar el navegador
        driver.quit()
