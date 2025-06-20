from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from conftest import driver

class TestNavigation:
    # Проверяем начальное состояние (изначально выбран раздел "Булки")
    def test_initial_selected_tab_rolls(self, driver):
        tab1 = driver.find_element(*Locators.BUTTON_ROLLS)
        assert 'current' in tab1.get_attribute('class')
        assert driver.find_element(*Locators.SECTION_ROLLS).text == 'Булки'

    # Проверяем переход в раздел "Соусы"
    def test_go_to_section_sauces(self, driver):
        tab2 = driver.find_element(*Locators.BUTTON_SAUCES)
        tab2.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_SAUCES))
        assert 'current' in tab2.get_attribute('class')
        assert driver.find_element(*Locators.SECTION_SAUCES).text == 'Соусы'

    # Проверяем переход в раздел "Начинки"
    def test_go_to_section_stuffings(self, driver):
        tab3 = driver.find_element(*Locators.BUTTON_STUFFINGS)
        tab3.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_STUFFINGS))
        assert 'current' in tab3.get_attribute('class')
        assert driver.find_element(*Locators.SECTION_STUFFINGS).text == 'Начинки'

    # Проверяем переход из раздела "Соусы" в раздел "Булки"
    def test_go_from_sauces_to_stuffings(self, driver):
        tab2 = driver.find_element(*Locators.BUTTON_SAUCES)
        tab2.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_SAUCES))
        assert 'current' in tab2.get_attribute('class')
        assert driver.find_element(*Locators.SECTION_SAUCES).text == 'Соусы'
        tab1 = driver.find_element(*Locators.BUTTON_ROLLS)
        tab1.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.SECTION_ROLLS))
        assert 'current' in tab1.get_attribute('class')
        assert driver.find_element(*Locators.SECTION_ROLLS).text == 'Булки'