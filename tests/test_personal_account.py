import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from constants import BASE_URL


class TestPersonalAccount:

    def test_navigate_to_personal_account(self, logged_in_user, driver):
        """Тест перехода в личный кабинет."""
        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем что открылся личный кабинет — элемент отображается
        profile_description = wait.until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION)
        )
        assert profile_description.is_displayed()

    def test_navigate_from_account_to_constructor(self, logged_in_user, driver):
        """Тест перехода в конструктор через кнопку."""
        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Проверяем что вернулись в конструктор — элемент отображается
        burger_title = wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_navigate_from_account_via_logo(self, logged_in_user, driver):
        """Тест перехода в конструктор через логотип."""
        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем на логотип
        driver.find_element(*MainPageLocators.LOGO).click()

        # Проверяем что вернулись в конструктор — элемент отображается
        burger_title = wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_logout_from_account(self, logged_in_user, driver):
        """Тест выхода из аккаунта."""
        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем кнопку "Выход"
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        # Проверяем что перешли на страницу входа — элемент отображается
        login_title = wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert login_title.is_displayed()
