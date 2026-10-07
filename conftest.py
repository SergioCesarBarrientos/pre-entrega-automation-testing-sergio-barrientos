import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """
    Crea una instancia independiente de Chrome para cada test.
    Selenium Manager se encarga de gestionar el WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()