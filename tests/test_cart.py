from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()
    
    # Agregar espera implícita para que el driver espere un tiempo antes de lanzar una excepción si no encuentra un elemento
    driver.implicitly_wait(5)

    try:
        # Login
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Agregar el primer producto al carrito
        producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        nombre_producto = producto.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        producto.find_element(By.TAG_NAME, "button").click()

        # Verificar que el carrito tenga 1 producto (o sea que el número en el ícono del carrito cambie a 1 al agregar el producto)
        numero_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert numero_carrito == "1", f"Se esperaba que el carrito tuviera 1 producto, pero tiene {numero_carrito}"
        
        # Navegar al carrito y verificar que el producto agregado figure
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        producto_carrito = driver.find_element(By.CLASS_NAME, "cart_item")
        assert producto_carrito.find_element(By.CLASS_NAME, "cart_item_name").text == nombre_producto, "El producto en el carrito no coincide con el producto agregado"

    finally:
        driver.quit()