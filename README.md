# 🧪 Automatización de Pruebas - SauceDemo

Proyecto de automatización de pruebas funcionales sobre la plataforma SauceDemo, utilizando Python, Pytest y Selenium WebDriver.

## 📋 Descripción

El proyecto implementa diferentes casos de prueba automatizados sobre SauceDemo.

Las pruebas permiten verificar:

- 🔐 Inicio de sesión con credenciales válidas.
- 🔄 Redirección correcta a la página de inventario.
- 📦 Presencia y visualización de productos.
- 🏷️ Nombre y precio del primer producto.
- 📋 Presencia del menú principal.
- 🔽 Presencia del filtro de productos.
- 🛒 Agregado de productos al carrito.
- 🔢 Actualización del contador del carrito.
- ✅ Verificación del producto agregado dentro del carrito.

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Pytest | Framework de testing |
| Selenium WebDriver | Automatización del navegador |
| pytest-html | Generación de reportes HTML |
| Git | Control de versiones |
| GitHub | Repositorio remoto |

## 📁 Estructura del proyecto

pre-entrega-automation-testing-sergio-barrientos/ 
│ ├── tests/ 
│ └── testsaucedemo.py 
│ ├── utils/ 
│ └── saucedemohelpers.py 
│ ├── assets/ 
│ └── style.css 
│ ├── reports/ 
│ ├── assets/ 
│ │ └── style.css 
│ ├── screenshots/ 
│ │ └── testagregarproductoalcarrito.png 
│ ├── reporte.html 
│ └── test_execution.log 
│ ├── conftest.py 
├── requirements.txt 
├── README.md 
└── .gitignore


### `tests/test_saucedemo.py`

Contiene los casos de prueba automatizados:

- Login exitoso.
- Navegación y validación del catálogo.
- Agregado y validación de productos en el carrito.

### `utils/saucedemo_helpers.py`

Contiene las funciones auxiliares utilizadas para evitar la repetición de código y facilitar el mantenimiento de las pruebas.

### `conftest.py`

Contiene el fixture encargado de crear y cerrar una instancia independiente del navegador para cada caso de prueba.

Además, gestiona el registro de logs y la generación automática de capturas de pantalla cuando un test falla.

### `requirements.txt`

Contiene las dependencias necesarias para ejecutar el proyecto.

### `reports/`

Contiene los resultados generados durante la ejecución de las pruebas:

- Reporte HTML generado mediante pytest-html.
- Capturas de pantalla automáticas en caso de fallos.
- Logs de ejecución de las pruebas.

## 🔑 Credenciales de prueba

Para realizar las pruebas se utilizan las credenciales proporcionadas por SauceDemo:

- **Usuario:** `standard_user`
- **Contraseña:** `secret_sauce`

## ⚙️ Instalación

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

### 1. Crear el entorno virtual

En Windows:

python -m venv venv


### 2. Activar el entorno virtual

En Windows:

venv\Scripts\activate


En Linux/Mac:

python3 -m venv venv source venv/bin/activate


### 3. Instalar las dependencias

pip install -r requirements.txt


## ▶️ Ejecución de las pruebas

Para ejecutar todos los casos de prueba:

pytest tests/test_saucedemo.py -v


También se puede utilizar:

python -m pytest tests/test_saucedemo.py -v


## 📊 Generación del reporte HTML

Para generar el reporte de las pruebas:

pytest tests/test_saucedemo.py -v --html=reports/reporte.html


Al finalizar la ejecución se generará el archivo:

reports/reporte.html


Este reporte permite visualizar de manera detallada el resultado de cada caso de prueba.

## 📸 Capturas y logs

En caso de que un test falle, el proyecto genera automáticamente una captura de pantalla dentro de:

reports/screenshots/


Los logs de ejecución se almacenan en:

reports/test_execution.log


De esta manera, el proyecto cuenta con evidencias adicionales para facilitar el análisis de errores durante la ejecución de las pruebas.

## 🧪 Casos de prueba

### 1. 🔐 Login exitoso

Verifica que el usuario pueda iniciar sesión correctamente.

Se validan:

- Ingreso con credenciales válidas.
- Redirección a `/inventory.html`.
- Título de la aplicación: `Swag Labs`.
- Presencia del encabezado `Products`.

### 2. 📦 Navegación y catálogo

Verifica el correcto funcionamiento de la página de inventario.

Se validan:

- Título de la página.
- Presencia de productos visibles.
- Nombre del primer producto.
- Precio del primer producto.
- Presencia del menú principal.
- Presencia del filtro de productos.

### 3. 🛒 Agregar producto al carrito

Verifica el funcionamiento básico del carrito de compras.

Se validan:

- Agregado del primer producto.
- Incremento del contador del carrito.
- Navegación a la página del carrito.
- Presencia del producto agregado.
- Coincidencia entre el producto seleccionado y el producto mostrado en el carrito.

## 🔄 Independencia de los tests

Cada caso de prueba utiliza una instancia independiente del navegador.

Además, cada test realiza nuevamente el proceso de login antes de ejecutar sus respectivas validaciones.

Esto permite garantizar que:

- Cada prueba comienza desde un estado conocido.
- La ejecución de un test no depende del resultado de otro.
- Una falla en un caso de prueba no afecta a los demás.

## ✅ Resultado de las pruebas

Los casos de prueba fueron ejecutados correctamente.

**Resultado obtenido:**

3 passed


Los tres escenarios automatizados finalizaron exitosamente:

testloginexitoso PASSED testnavegacionycatalogo PASSED testagregarproductoal_carrito PASSED


También se generó correctamente el reporte HTML mediante pytest-html.

## 📌 Control de versiones

El proyecto utiliza Git para el control de versiones y GitHub como repositorio remoto.

Durante el desarrollo se realizan commits descriptivos para registrar los diferentes avances del proyecto.