# Appium Python — POM + Sauce Labs

Suite de automatización móvil Android con Appium y Python, estructurada bajo el patrón **Page Object Model (POM)** con soporte para ejecución local y en **Sauce Labs**.

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.10+ | Lenguaje base |
| Appium 2.x | Servidor de automatización móvil |
| UIAutomator2 | Driver Android |
| pytest | Framework de pruebas |
| allure-pytest | Reportes con evidencia visual |
| hypothesis | Property-based testing |
| python-dotenv | Gestión de credenciales via `.env` |
| Sauce Labs | Ejecución en la nube (us-west-1) |

---

## Estructura del proyecto (POM)

```
proyecto/
│
├── pages/                        # Capa de Page Objects
│   ├── __init__.py
│   ├── base_page.py              # Clase base con utilidades de espera
│   ├── home_page.py              # Pantalla principal de ApiDemos
│   ├── app_page.py               # Submenú App
│   ├── search_page.py            # Submenú Search
│   ├── invoke_search_page.py     # Pantalla Invoke Search
│   ├── fragment_page.py          # Submenú Fragment
│   ├── nesting_tabs_page.py      # Pantalla Nesting Tabs
│   ├── preference_page.py         # Pantalla Preference (NUEVO)
│   └── animation_page.py          # Pantalla Animation (NUEVO)
│
├── test/                          # Capa de pruebas
│   ├── test_appiumdemo.py         # Tests para ejecución LOCAL
│   ├── test_appiumdemo_saucelabs.py # Tests para ejecución SAUCE LABS
│   ├── test_config_properties.py  # Property-based tests de Config
│   └── scenarios.py               # Escenarios compartidos entre entornos
│
├── apps/
│   └── ApiDemos-debug.apk        # APK bajo prueba
│
├── config.py                     # Clase Config (local / saucelabs)
├── conftest.py                   # Fixtures driver y driver_saucelabs
├── scenarios.py                  # Lógica de escenarios reutilizable
├── pytest.ini                    # Configuración de pytest y marks
├── .env                          # Credenciales (NO subir al repo)
├── .env.example                  # Plantilla de variables de entorno
├── requirements.txt              # Dependencias Python
└── Readme.md
```

### Responsabilidades por capa

- **`pages/`** — encapsula localizadores e interacciones de UI. Los tests nunca acceden directamente a elementos.
- **`config.py`** — decide el entorno (local o Sauce Labs) y construye las capabilities del driver.
- **`conftest.py`** — provee los fixtures `driver` (local) y `driver_saucelabs`.
- **`scenarios.py`** — contiene la lógica de cada escenario, reutilizable en ambos entornos.
- **`test/`** — orquesta los escenarios y declara aserciones.

---

## Prerrequisitos

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

### 2. Crear y activar entorno virtual Python

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

> Sabrás que está activo cuando el prompt muestre `(venv)` al inicio.

### 3. Instalar dependencias del proyecto

```bash
pip install -r requirements.txt
```

### 4. Validar instalación

```bash
python --version
pytest --version
appium --version
```

### Appium (Node.js requerido)

```bash
npm install -g appium
appium driver install uiautomator2
appium -v
```

### Android SDK

1. Instala Android Studio desde https://developer.android.com/studio
2. En **SDK Manager** activa:
   - Android SDK Build-Tools
   - Android SDK Platform-Tools
   - Android SDK Command-line Tools (latest)
3. Configura variables de entorno:

```
ANDROID_HOME = C:\Users\USUARIO\AppData\Local\Android\Sdk

Path (agregar):
  %ANDROID_HOME%\platform-tools
  %ANDROID_HOME%\emulator
  %ANDROID_HOME%\cmdline-tools\latest\bin
```

4. Valida:

```bash
adb devices
emulator -list-avds
```

---

## Configuración del archivo `.env`

Copia `.env.example` como `.env` y completa los valores:

```bash
copy .env.example .env
```

Contenido del `.env`:

```env
# Entorno: local | saucelabs
APPIUM_ENV=local

# Solo necesario cuando APPIUM_ENV=saucelabs
SAUCE_USERNAME=tu_usuario
SAUCE_ACCESS_KEY=tu_access_key
```

> **Importante:** nunca subas `.env` al repositorio. Agrega `.env` a tu `.gitignore`.

---

## Ejecución de pruebas

> Asegúrate de tener el entorno virtual activado antes de correr cualquier comando:
> ```bash
> # Windows
> venv\Scripts\activate
> # Mac/Linux
> source venv/bin/activate
> ```

### Local

Requisitos previos:
- Emulador `Pixel_9` corriendo: `emulator -avd Pixel_9`
- Servidor Appium corriendo: `appium`

```bash
# Asegúrate que .env tiene APPIUM_ENV=local
pytest test/test_appiumdemo.py -v --alluredir=allure-results
```

### Sauce Labs

Requisitos previos:
- APK subido al storage de Sauce Labs
- Credenciales en `.env`

```bash
# Cambia en .env: APPIUM_ENV=saucelabs y completa SAUCE_USERNAME y SAUCE_ACCESS_KEY
pytest test/test_appiumdemo_saucelabs.py -v --alluredir=allure-results
```

### Property-based tests (sin driver)

```bash
pytest test/test_config_properties.py -v
```

### Todos los tests

```bash
pytest -v --alluredir=allure-results
```

---

## Escenarios Incluidos

### 1. Invoke Search and Back Home
**Archivo:** `scenario_invoke_search_and_back_home` en `scenarios.py`

**Flujo:**
```
Home → App → Search → Invoke Search → [Introduce texto] → Volver 3 niveles a Home
```

**Qué prueba:**
- Navegación de 3 niveles de menú
- Interacción con campo de texto (input)
- Navegación hacia atrás (back button)
- Validación de pantalla inicial

**Tests:**
- Local: `test/test_appiumdemo.py::test_invoke_search_and_back_home`
- Sauce Labs: `test/test_appiumdemo_saucelabs.py::test_invoke_search_and_back_home_sl`

---

### 2. Select Checks and Back
**Archivo:** `scenario_select_checks_and_back` en `scenarios.py`

**Flujo:**
```
Home → App → Fragment → Nesting Tabs → [Selecciona checkboxes] → Volver a Fragment
```

**Qué prueba:**
- Navegación a submenu
- Interacción con checkboxes
- Selección múltiple de elementos
- Navegación hacia atrás

**Tests:**
- Local: `test/test_appiumdemo.py::test_select_checks_and_back`
- Sauce Labs: `test/test_appiumdemo_saucelabs.py::test_select_checks_and_back_sl`

---

### 3. Navigate Preference Menu ⭐ NUEVO
**Archivo:** `scenario_navigate_preference_menu` en `scenarios.py`

**Flujo:**
```
Home → Preference → Switch → Volver a Home
```

**Qué prueba:**
- Navegación directa desde Home a Preference
- Interacción con opciones de preferencia
- Validación de pantalla en Switch
- Cierre con navegación hacia atrás

**Page Object:** `pages/preference_page.py`
- `is_displayed()` —  Verifica que la opcion Switch en Preference está visible
- `interact_with_option()` — Interactua con la opcion Switch


**Tests:**
- Local: `test/test_appiumdemo.py::test_navigate_preference_menu`
- Sauce Labs: `test/test_appiumdemo_saucelabs.py::test_navigate_preference_menu`

---

### 4. Explore Animation Feature ⭐ NUEVO
**Archivo:** `scenario_explore_animation_feature` en `scenarios.py`

**Flujo:**
```
Home → Animation → Verifica elemento de animación: Events → Volver 2 niveles a Home
```

**Qué prueba:**
- Navegación a pantalla con elementos dinámicos (Animation)
- Validación de pantalla Animation
- Verificación de existencia de elementos interactivos
- Navegación hacia atrás desde submenu

**Page Object:** `pages/animation_page.py`
- `is_displayed()` — Verifica que la opcion de animacion: Events, está  visible
- `go_to_option_animation()` — Interactua con la opcion Events.
- `is_displayed_button()` — Verifica que el boton está  visible.
- `verify_animation_is_running()` — Interactua con el boton Play.


**Localizadores:**
```python
_ANIMATION_ELEMENT = (AppiumBy.ACCESSIBILITY_ID, "Events")
_PLAY_BUTTON = (AppiumBy.ID, "io.appium.android.apis:id/startButton")
```

**Tests:**
- Local: `test/test_appiumdemo.py::test_explore_animation_feature`
- Sauce Labs: `test/test_appiumdemo_saucelabs.py::test_explore_animation_feature`

---

## Ejecución de Tests Específicos

```bash
# Ejecutar solo los nuevos escenarios (LOCAL)
pytest test/test_appiumdemo.py::test_navigate_preference_menu -v --alluredir=allure-results
pytest test/test_appiumdemo.py::test_explore_animation_feature -v --alluredir=allure-results

# Ejecutar solo los nuevos escenarios (SAUCE LABS)
pytest test/test_appiumdemo_saucelabs.py::test_navigate_preference_menu -v --alluredir=allure-results
pytest test/test_appiumdemo_saucelabs.py::test_explore_animation_feature -v --alluredir=allure-results

# Ejecutar todos con tag específico
pytest -m saucelabs -v --alluredir=allure-results
pytest -m local -v --alluredir=allure-results
```

---

## Reporte Allure

```bash
allure serve allure-results
```

Abre el navegador automáticamente con:
- Pasos de cada test
- Screenshot al finalizar cada test
- Screenshot del estado en caso de fallo
- Duración y estado por escenario

---

## Ver resultados en Sauce Labs

1. Entra a https://app.saucelabs.com
2. Ve a **Automated → Test Results**
3. Filtra por build: `appium-pom-saucelabs`
4. Cada sesión incluye video grabado, logs de Appium y screenshots

---

## Agregar un nuevo escenario

1. Si involucra una pantalla nueva, crea `pages/nueva_pantalla.py` heredando de `BasePage`
2. Agrega la función del escenario en `scenarios.py`
3. Llama el escenario desde `test/test_apidemos.py` (local) y `test/test_apidemos_saucelabs.py` (Sauce Labs)

---

## Documentación de Desarrollo

Para entender cómo se crearon los nuevos escenarios y cómo agregar más:

- **`GUIA_COMPLETA_CREACION_ESCENARIOS.md`** — Guía completa sobre arquitectura POM, escenarios y tests
- **`IDENTIFICAR_ELEMENTOS_PASO_A_PASO.md`** — Cómo usar Appium Inspector para encontrar elementos
- **`CREAR_PAGE_OBJECTS_DETALLADO.md`** — Cómo crear Page Objects siguiendo el patrón POM
- **`INICIO_RAPIDO.md`** — Plan de trabajo paso a paso para crear nuevos escenarios
- **`COMO_AGREGAR_CASO.md`** — Referencia rápida para agregar nuevos casos de prueba

---

## Buenas prácticas POM

- Los localizadores viven **solo** en el Page Object correspondiente
- Los Page Objects exponen **métodos de acción**, no elementos crudos
- Los métodos de navegación retornan el Page Object de la pantalla destino (encadenamiento)
- Las esperas son **internas** al Page Object — los tests no usan `WebDriverWait` directamente
- Usa `ACCESSIBILITY_ID` cuando sea posible, `ID` como segunda opción, `XPATH` como último recurso
- Cada Page Object **DEBE** tener `is_displayed()` para validar que estamos en la pantalla correcta
- Los escenarios en `scenarios.py` son **reutilizables** en tests locales y Sauce Labs

---

## Contribución: Agregar Nuevo Escenario

Para agregar un nuevo escenario siguiendo el patrón:

1. **Identifica los elementos** con Appium Inspector
2. **Crea el Page Object** en `pages/nueva_pantalla.py` heredando de `BasePage`
3. **Agrega el escenario** en `scenarios.py` con pasos usando `@allure.step()`
4. **Agrega los tests** en `test/test_appiumdemo.py` y `test/test_appiumdemo_saucelabs.py`
5. **Ejecuta y valida** con `pytest` y revisa el reporte Allure

Ver `COMO_AGREGAR_CASO.md` para instrucciones detalladas.
