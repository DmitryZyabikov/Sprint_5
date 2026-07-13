import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators, MainPageLocators


class TestConstructor:

    def test_navigate_to_buns_section(self, driver):
        # Проверка перехода к булкам
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Ждем загрузки
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Сначала кликаем на соусы
        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()
        wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_SECTION))

        # Потом возвращаемся к булкам
        driver.find_element(*ConstructorLocators.BUNS_TAB).click()

        # Проверяем что перешли к булкам
        buns_section = wait.until(EC.visibility_of_element_located(ConstructorLocators.BUNS_SECTION))
        assert buns_section.text == "Булки"

    def test_navigate_to_sauces_section(self, driver):
        # Проверка перехода к соусам
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Ждем загрузки
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Кликаем на соусы
        driver.find_element(*ConstructorLocators.SAUCES_TAB).click()

        # Проверяем что перешли к соусам
        sauces_section = wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_SECTION))
        assert sauces_section.text == "Соусы"

    def test_navigate_to_fillings_section(self, driver):
        # Проверка перехода к начинкам
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Ждем загрузки
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Кликаем на начинки
        driver.find_element(*ConstructorLocators.FILLINGS_TAB).click()

        # Проверяем что перешли к начинкам
        fillings_section = wait.until(EC.visibility_of_element_located(ConstructorLocators.FILLINGS_SECTION))
        assert fillings_section.text == "Начинки"
