"""
Escenarios de prueba compartidos entre entornos local y Sauce Labs.
Cada función recibe un driver ya inicializado y ejecuta el flujo completo.
"""
import allure
from pages.home_page import HomePage
from pages.base_page import BasePage

def scenario_invoke_search_and_back_home(driver):
    """Navega App → Search → Invoke Search, introduce texto y verifica Home."""
    home = HomePage(driver)

    with allure.step("Navegar a App > Search > Invoke Search"):
        invoke_search = (
            home
            .go_to_app()
            .go_to_search()
            .go_to_invoke_search()
        )

    with allure.step("Introducir texto en el campo de búsqueda"):
        invoke_search.enter_query("hola")

    with allure.step("Volver 3 niveles hasta Home"):
        driver.back()
        driver.back()
        driver.back()

    with allure.step("Verificar que la pantalla Home está visible"):
        assert home.is_displayed(), "La pantalla Home no está visible tras volver"


def scenario_select_checks_and_back(driver):
    """Navega App → Fragment → Nesting Tabs, selecciona checkboxes y verifica Fragment."""
    home = HomePage(driver)

    with allure.step("Navegar a App > Fragment"):
        fragment_page = (
            home
            .go_to_app()
            .go_to_fragment()
        )

    with allure.step("Navegar a Nesting Tabs y seleccionar ambos checkboxes"):
        nesting = fragment_page.go_to_nesting_tabs()
        nesting.select_check1_if_unchecked().select_check2_if_unchecked()

    with allure.step("Volver a Fragment"):
        returned_fragment = nesting.go_back()

    with allure.step("Verificar que la pantalla Fragment está visible"):
        assert returned_fragment.is_displayed(), "La pantalla Fragment no está visible tras volver"

def scenario_navigate_preference_menu(driver):
    """
    Navega home--> Preference --> selecciona opcion --> verifica --> Vueleve Home
    """
    
    home = HomePage(driver)
    
    with allure.step("Navegar Preference"):
        preference_page = home.go_to_preference()
        
    with allure.step("Verificar que la pantalla Preference está  visible."):
        assert preference_page.is_displayed(), "Preference no está visible"
    
    with allure.step("Interactua con una opción de preferencia"):
        preference_page.interact_with_option()
    
    with allure.step("Volver al Home usando navegación  hacia atras"):
        driver.back() #Volvemos a Preference
        driver.back() #Volvemos a Home
        assert home.is_displayed(),"Home no está visible tras volver"
        
    
def scenario_explore_animation_feature(driver):
    """
    Navegar Home + Animation + verifica animación + Vuelve Home
    """
    home = HomePage(driver)
        
    with allure.step('Navegar a Animation'):
        animation_page =  home.go_to_animation()
               
        with allure.step('Verificar que la opcion de Animation está  visible.'):
            assert animation_page.is_displayed(), "La opcion de Animation:Eventos, no esta visible."
        
        with allure.step('Ir a la pantalla de la opcion en Animation'):
            opcion = animation_page.go_to_option_animation()
            assert opcion, "Elemento de animación no encontrado"
        
          
        with allure.step("Verificar que el boton está presente."):
            is_present = animation_page.is_displayed_button()
            assert is_present, "Botón de control no encontrado"
        
        with allure.step("Verificar que la animacion está corriendo."):
            animation_running = animation_page.verify_animation_is_running()
            assert animation_running, "Verifica que la animación está corriendo"
        
        
        with allure.step("Volver al Home"):
            driver.back() # Vuelve a Animation
            driver.back() # Vuelve al Home
            assert home.is_displayed(), "Home no está visible tras volver"