import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from conftest import driver

class TestNavigation:
    # Проверяем переходы в разделы
    @pytest.mark.parametrize("button_locator, section_locator", [
        (Locators.BUTTON_ROLLS, Locators.SECTION_ROLLS),
        (Locators.BUTTON_SAUCES, Locators.SECTION_SAUCES),
        (Locators.BUTTON_STUFFINGS, Locators.SECTION_STUFFINGS)
    ])
    def test_tab_navigation(self, driver, button_locator, section_locator):
        button = driver.find_element(*button_locator)
        button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(section_locator))
        assert 'current' in button.get_attribute('class')
        assert driver.find_element(*section_locator).is_displayed()

    # Проверяем переход из раздела "Соусы" в раздел "Булки"
    def test_go_from_sauces_to_stuffings(self, driver):
        tab2 = driver.find_element(*Locators.BUTTON_SAUCES)
        tab2.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_SAUCES))
        assert 'current' in tab2.get_attribute('class')
        assert driver.find_element(Locators.SECTION_SAUCES).is_displayed()
        tab1 = driver.find_element(*Locators.BUTTON_ROLLS)
        tab1.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_ROLLS))
        assert 'current' in tab1.get_attribute('class')
        assert driver.find_element(Locators.SECTION_ROLLS).is_displayed()
