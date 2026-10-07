from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.saucedemo_helpers import (
    login_to_saucedemo,
    get_first_product,
    add_first_product_to_cart,
    get_cart_count,
    open_cart,
)


def test_login_exitoso(driver):
    """
    Verifica que un usuario válido pueda iniciar sesión
    correctamente en SauceDemo.
    """

    login_to_saucedemo(driver)

    # Validar que la URL corresponda a la página de inventario
    assert "/inventory.html" in driver.current_url

    # Validar que aparezca el título de la aplicación
    assert driver.title == "Swag Labs"

    # Validar que esté presente el encabezado Products
    products_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".title")
        )
    )

    assert products_title.text == "Products"


def test_navegacion_y_catalogo(driver):
    """
    Verifica el título de la página, la presencia de productos
    y los elementos principales del catálogo.
    """

    login_to_saucedemo(driver)

    # Validar título de la página
    assert driver.title == "Swag Labs"

    # Validar que estamos en inventario
    assert "/inventory.html" in driver.current_url

    # Verificar que exista al menos un producto visible
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )

    assert len(products) > 0

    # Obtener y mostrar información del primer producto
    product_name, product_price = get_first_product(driver)

    print(f"Primer producto: {product_name}")
    print(f"Precio: {product_price}")

    assert product_name != ""
    assert product_price != ""

    # Validar menú principal
    menu_button = driver.find_element(
        By.ID, "react-burger-menu-btn"
    )

    assert menu_button.is_displayed()

    # Validar filtro de productos
    product_filter = driver.find_element(
        By.CSS_SELECTOR, ".product_sort_container"
    )

    assert product_filter.is_displayed()


def test_agregar_producto_al_carrito(driver):
    """
    Verifica que se pueda agregar el primer producto al carrito
    y que aparezca correctamente en el carrito
    """

    login_to_saucedemo(driver)

    # Guardamos el nombre del producto antes de agregarlo
    product_name, _ = get_first_product(driver)

    # Agregar el primer producto
    add_first_product_to_cart(driver)

    # Verificar que el contador del carrito sea 1
    cart_count = get_cart_count(driver)

    assert cart_count == 1

    # Navegar al carrito.
    open_cart(driver)

    # Validar que estamos en la página del carrito
    assert "/cart.html" in driver.current_url

    # Buscar el producto dentro del carrito.
    cart_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
        )
    )

    # Verificar que sea el mismo producto agregado
    assert cart_product.text == product_name