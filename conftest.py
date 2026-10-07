import logging
from pathlib import Path

import pytest
from selenium import webdriver


# Directorios donde se almacenan los reportes y evidencias.
REPORTS_DIR = Path("reports")
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

REPORTS_DIR.mkdir(exist_ok=True)
SCREENSHOTS_DIR.mkdir(exist_ok=True)


# Configuración del archivo de logs.
logging.basicConfig(
    filename=REPORTS_DIR / "test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@pytest.fixture
def driver(request):
    """
    Crea una instancia independiente de Chrome para cada test.
    Selenium Manager se encarga de gestionar el WebDriver.
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    logging.info("Iniciando test: %s", request.node.name)

    yield browser

    # Si el test falla, intenta guardar una captura.
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_path = (
            SCREENSHOTS_DIR / f"{request.node.name}.png"
        )

        try:
            browser.save_screenshot(str(screenshot_path))

            logging.error(
                "El test %s falló. Captura guardada en: %s",
                request.node.name,
                screenshot_path,
            )

        except Exception as error:
            logging.error(
                "No fue posible guardar la captura del test %s: %s",
                request.node.name,
                error,
            )

    logging.info("Finalizando test: %s", request.node.name)

    try:
        browser.quit()
    except Exception as error:
        logging.warning(
            "No fue posible cerrar correctamente el navegador: %s",
            error,
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Guarda el resultado de cada fase de ejecución del test
    para poder detectar si el test falló.
    """

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)