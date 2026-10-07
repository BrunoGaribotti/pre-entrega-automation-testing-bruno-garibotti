from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


def login(driver, usuario="standard_user", password="secret_sauce"):
    driver.get(URL)
    espera = WebDriverWait(driver, 10)
    espera.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    espera.until(EC.url_contains("/inventory.html"))