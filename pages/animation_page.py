from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class AnimationPage(BasePage):
    """Page Object de la pantalla Animation."""
    
    _ANIMATION_ELEMENT = (AppiumBy.ACCESSIBILITY_ID,"Events")
    _PLAY_BUTTON = (AppiumBy.ID, "io.appium.android.apis:id/startButton")  

    def is_displayed(self) -> bool:
        """Verifica que la opcion de animacion está  visible"""
        return self.is_element_present(self._ANIMATION_ELEMENT)
    
    def go_to_option_animation(self) -> "AnimationPage":
        """Interactua con la opcion Events."""
        self.wait_and_click(self._ANIMATION_ELEMENT )
        return self
    
    def is_displayed_button(self) -> bool:
        """Verifica que el boton está  visible"""
        return self.is_element_present(self._PLAY_BUTTON)
    
    def verify_animation_is_running(self) -> bool:
        """Interactua con el boton Play."""        
        self.wait_and_click(self._PLAY_BUTTON)
        return self            
    
    
    