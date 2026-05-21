# 📊 Evidencias: Creación de 2 Nuevos Escenarios de Automatización Mobile

**Proyecto:** Automatización Mobile - My Demo App  
**Fecha:** Mayo 2026  
**Autor:** Caro (carolina.rodriguez.guerra@gmail.com)  
**Framework:** Appium + Python + Page Object Model (POM)

---

## ✅ Objetivo Completado

Crear **2 nuevos escenarios** de automatización móvil siguiendo Page Object Model profesional, ejecutables en **SauceLabs**.

---

## 📋 Escenarios Creados

### Escenario 1: Navigate Preference Menu
#### Descripción
Navega desde la pantalla Home directamente a la pantalla Preference, selecciona una opción y vuelve a Home validando la navegación.

#### Viabilidad de Automatización
| Criterio | Análisis | Viable |
|----------|----------|--------|
| **¿Elementos identificables?** | Todos los elementos (Preference, opciones) tienen accessibility IDs | ✅ Sí |
| **¿Flujo predecible?** | El flujo es lineal: Home → Preference → Opcion 9. Switch → volver | ✅ Sí |
| **¿Verificable?** | Se puede validar con `is_displayed()` y asserts | ✅ Sí |
| **¿Repetible?** | El mismo flujo se ejecuta idénticamente cada vez | ✅ Sí |
| **¿Valor de negocio?** | Prueba que el acceso a preferencias funciona correctamente | ✅ Sí |

#### Flujo de Usuario
```
1. Usuario inicia en Home
2. Usuario hace click en "Preference"
3. Sistema navega a pantalla Preference
4. Usuario selecciona una opción: 9. Switch
5. Usuario presiona botón atrás
6. Sistema regresa a Home
7. Verificación: Home está visible
```

#### Arquitectura
```
home_page.py
├─ go_to_preference() → PreferencePage

preference_page.py
├─ is_displayed() ✓
├─ interact_with_option() ✓
└─ go_back() → HomePage

scenarios.py
└─ scenario_navigate_preference_menu(driver) ✓

test_appiumdemo_saucelabs.py
└─ test_navigate_preference_menu(driver_saucelabs) ✓
```

#### Identificación de Elementos

<figure align="center">
  <img src="screenshots/Preference/Preference Option (Appium Inspector).png" alt="Preference en Home" width="400" height="400">
<figcaption>Identificación de la etiqueta Preference en Appium Inspector</figcaption>
</figure>

<figure align="center">
  <img src="screenshots/Preference/Switch Option (Appium Inspector).png" alt="Switch en Preference" width="400" height="400">
<figcaption>Identificación de la etiqueta Switch en Appium Inspector</figcaption>
</figure>

#### Localizadores Identificados
```python
# En HomePage
_PREFERENCE = (AppiumBy.ACCESSIBILITY_ID, "Preference")

# En PreferencePage  
 _SOME_OPTION = (AppiumBy.ACCESSIBILITY_ID,"9. Switch") # Opción seleccionable
```

#### Resultado de Ejecución
```
✅ PASSED - Ejecutado en Sauce Labs
✅ Pasos Allure: 4
```

<figure align="center">
  <img src="screenshots/Preference/Result Preference Option (SauceLabs Video).png" alt="Sauce" width="400" height="400">
<figcaption>Pantalla Final Video en SauceLabs</figcaption>
</figure>

<figure align="center">
  <img src="screenshots/Preference/test_navigate_preference_menu (Allure).png" alt="Allure" width="400" height="400">
<figcaption>Test Navigate Preference Menu (Allure)</figcaption>
</figure>

---

### Escenario 2: Explore Animation Feature
#### Descripción
Navega desde Home → Animation, verifica que la opcion Events existe -> Verifica que el boton Play esta disposible y da clic en esta opcion, luego vuelve a Home.

#### Viabilidad de Automatización
| Criterio | Análisis | Viable |
|----------|----------|--------|
| **¿Elementos identificables?** | "Events" (ACCESSIBILITY_ID) y "startButton" (ID) identificados | ✅ Sí |
| **¿Flujo predecible?** | Navegación clara: Home →  Animation → validar → volver | ✅ Sí |
| **¿Verificable?** | Se verifica presencia de elementos interactivos | ✅ Sí |
| **¿Repetible?** | Flujo consistente en cada ejecución | ✅ Sí |
| **¿Valor de negocio?** | Valida que la pantalla Animation y sus controles funcionan | ✅ Sí |

#### Flujo de Usuario
```
1. Usuario inicia en Home
2. Usuario hace click en "Animation"
3. Sistema navega a menú Animation
4. Sistema verifica que el elemento "Events" existe
5. Usuario hace click en "Events"
6. Sistema navega la pantalla de Events.
7. Sistema verifica que el botón "startButton" existe
8. El usuario da clic en el botón "startButton"
9. Usuario presiona atrás 2 veces
10. Sistema regresa a Home
11. Verificación: Home está visible
```

#### Localizadores Identificados
```python
# En Home
_ANIMATION = (AppiumBy.ACCESSIBILITY_ID, "Animation")

# En AnimationPage
_ANIMATION_ELEMENT = (AppiumBy.ACCESSIBILITY_ID, "Events")
_PLAY_BUTTON = (AppiumBy.ID, "io.appium.android.apis:id/startButton")
```

#### Resultado de Ejecución
```
✅ PASSED - Ejecutado en Sauce Labs
✅ Pasos Allure: 5
```

<figure align="center">
  <img src="screenshots/Animation/Result Animation Option (SauceLabs Video).png" alt="Sauce" width="400" height="400">
<figcaption>Pantalla Final Video en SauceLabs</figcaption>
</figure>

<figure align="center">
  <img src="screenshots/Preference/test_explore_animation_feature (Allure).png" alt="Allure" width="400" height="400">
<figcaption>Test Explore Animation Feature (Allure)</figcaption>
</figure>

---


## 🏗️ Estructura Final del Proyecto

```
Pro_appium_python_pom/
├── pages/
│   ├── base_page.py
│   ├── home_page.py              (Modificado)
│   ├── app_page.py              
│   ├── search_page.py
│   ├── fragment_page.py
│   ├── invoke_search_page.py
│   ├── nesting_tabs_page.py
│   ├── preference_page.py         (Nuevo)
│   └── animation_page.py          (Nuevo)
│
├── test/
│   ├── test_appiumdemo.py         (Modificado)
│   ├── test_appiumdemo_saucelabs.py (Modificado)
│   └── test_config_properties.py
│
├── scenarios.py                   (Modificado)
├── config.py
├── conftest.py
├── requirements.txt
├── pytest.ini
├── Readme.md                      (Modificado)
│
├── 📚 DOCUMENTACIÓN DE APRENDIZAJE
└── EVIDENCIAS_ESCENARIOS_NUEVOS.md           (Nuevo)
```

---

## 🎯 Métodos Implementados

### PreferencePage
```python
def is_displayed(self) -> bool
    └─ Valida que pantalla Preference está visible ✓

def interact_with_option(self) -> "PreferencePage"
    └─ Selecciona opción de preferencia (fluent interface) ✓

```

### AnimationPage
```python
def is_displayed(self) -> bool
    └─ Valida que pantalla Animation está visible ✓
    
def go_to_option_animation(self) -> "AnimationPage"
     └─ Interactua con la opcion Events. ✓

def is_displayed_button(self) -> bool:
    └─Verifica que el boton está  visible.  ✓ 
    
def verify_animation_is_running(self) -> bool
    └─ Interactua con el boton Play. ✓

```

### HomePage (Actualizada)
```python
def go_to_preference(self)
    └─ Navega a PreferencePage ✓ (NUEVO)
```

### AppPage (Actualizada)
```python
def go_to_animation(self)
    └─ Navega a AnimationPage ✓ (NUEVO)
```

---


## 🧪 Ejecución y Validación

### Tests Sauce Labs
```bash
pytest test/test_appiumdemo_saucelabs.py -v --alluredir=allure-results
# Resultado: ✅ PASSED
```

### Reporte Allure
```bash
allure serve allure-results
```

### Resultados Visual Code

<figure align="center">
  <img src="screenshots/Results on Visual Studio Code .png" alt="Results VSC" width="400" height="400">
<figcaption>Resultados en visual code (4 Passed)</figcaption>
</figure>

---

### Resultados SauceLabs

<figure align="center">
  <img src="screenshots/Results on SauceLabs.png" alt="Results Sauce" width="400" height="400">
<figcaption>Resultados en SauceLabs (4 Completed)</figcaption>
</figure>

---
### Resultados Allure

<figure align="center">
  <img src="screenshots/Allure report.png" alt="Allure" width="400" height="400">
<figcaption>Allure report</figcaption>
</figure>


---