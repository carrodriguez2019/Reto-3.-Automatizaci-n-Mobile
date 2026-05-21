from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object de la pantalla principal de ApiDemos."""

    _ACCESSIBILITY = (AppiumBy.ACCESSIBILITY_ID, "Accessibility")
    _APP = (AppiumBy.ACCESSIBILITY_ID, "App")
    _PREFERENCE = (AppiumBy.ACCESSIBILITY_ID, "Preference") 
    _ANIMATION = (AppiumBy.ACCESSIBILITY_ID,"Animation")

    def is_displayed(self) -> bool:
        """Verifica que la pantalla Home está visible."""
        return self.is_element_present(self._ACCESSIBILITY)

    def go_to_app(self):
        """Navega al submenú App y retorna AppPage."""
        from pages.app_page import AppPage
        self.wait_and_click(self._APP)
        return AppPage(self.driver)
    
    def go_to_preference(self):
        """Navega a Preference y retorna"""
        from pages.preference_page import PreferencePage       
        self.wait_and_click(self._PREFERENCE)
        return PreferencePage(self.driver)
    
    def go_to_animation(self):
        """Navega a Animation y retorna AnimationPage"""
        from pages.animation_page import AnimationPage
        self.wait_and_click(self._ANIMATION)
        return AnimationPage(self.driver)
