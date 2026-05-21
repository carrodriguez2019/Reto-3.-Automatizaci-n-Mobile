from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class PreferencePage(BasePage):
    """Page Object de la pantalla Preference"""
    
    #1. Localizadores privados de clase
    #   Nombre: _ELEMENTO_DESCRIPTIVO
    #   Formato: (AppiumBy.TIPO, "valor")
    
    _SOME_OPTION = (AppiumBy.ACCESSIBILITY_ID,"9. Switch")
        
    def is_displayed(self) -> bool:
        """
        Verifica que la opcion Switch en Preference está visible.        
        """
        return self.is_element_present(self._SOME_OPTION)
    
    def interact_with_option(self) -> "PreferencePage":
        """Interactua con la opcion Switch."""
        self.wait_and_click(self._SOME_OPTION)
        return self
    
    
                