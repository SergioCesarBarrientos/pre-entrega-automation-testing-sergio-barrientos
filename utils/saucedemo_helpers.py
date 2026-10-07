from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def wait_for_element(driver, locator, timeout=10):
    """
    Espera explícitamente hasta que un elemento sea visible.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def login_to_saucedemo(driver):
    """
    Realiza el login utilizando las credenciales válidas
    proporcionadas por SauceDemo.
    """
    driver.get(BASE_URL)

    username_input = wait_for_element(
        driver, (By.ID, "user-name")
    )
    password_input = wait_for_element(
        driver, (By.ID, "password")
    )

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    login_button = wait_for_element(
        driver, (By.ID, "login-button")
    )
    login_button.click()

    # esperar que la página de inventario este disponible
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )


def get_first_product(driver):
    """
    Obtiene el nombre y precio del primer producto
    visible en el catálogo.
    """
    first_product = wait_for_element(
        driver, (By.CSS_SELECTOR, ".inventory_item")
    )

    product_name = first_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_name"
    ).text

    product_price = first_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_price"
    ).text

    return product_name, product_price


def add_first_product_to_cart(driver):
    """
    Agrega el primer producto disponible al carrito.
    """
    first_product = wait_for_element(
        driver, (By.CSS_SELECTOR, ".inventory_item")
    )

    add_button = first_product.find_element(
        By.CSS_SELECTOR, "button"
    )

    add_button.click()


def get_cart_count(driver):
    """
    Obtiene la cantidad indicada en el contador del carrito.
    """
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping_cart_badge")
        )
    )

    return int(cart_badge.text)


def open_cart(driver):
    """
    Navega al carrito de compras.
    """
    cart_button = wait_for_element(
        driver, (By.CSS_SELECTOR, ".shopping_cart_link")
    )

    cart_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )