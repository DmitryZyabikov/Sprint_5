import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators, MainPageLocators

# Константа с URL главной страницы
BASE_URL = "https://stellarburgers.education-services.ru"


class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        # Проверка перехода к булкам
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Сначала кликаем на соусы
        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
        wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_SECTION))

        # Потом возвращаемся к булкам
        driver.find_element(*ConstructorLocators.BUNS_TAB).click()

        # Проверяем, что вкладка "Булки" стала активной (по классу)
        active_tab = wait.until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB)
        )
        assert "tab_tab_type_current" in active_tab.get_attribute("class")

    def test_navigate_to_sauces_section(self, driver):
        # Проверка перехода к соусам
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Кликаем на соусы
        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

        # Проверяем, что вкладка "Соусы" стала активной
        active_tab = wait.until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB)
        )
        assert "tab_tab_type_current" in active_tab.get_attribute("class")

    def test_navigate_to_fillings_section(self, driver):
        # Проверка перехода к начинкам
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Кликаем на начинки
        driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

        # Проверяем, что вкладка "Начинки" стала активной
        active_tab = wait.until(
            EC.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB)
        )
        assert "tab_tab_type_current" in active_tab.get_attribute("class")