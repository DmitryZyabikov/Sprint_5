import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators, RestorePasswordPageLocators
from constants import BASE_URL, FORGOT_PASSWORD_URL


class TestLogin:
    def test_login_via_main_page_button(self, logged_in_user, driver):
        """Тест входа через кнопку 'Войти в аккаунт' на главной странице."""
        wait = WebDriverWait(driver, 15)

        # Переходим на главную
        driver.get(BASE_URL)

        # Нажимаем кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Заполняем форму
        email, password, name = logged_in_user
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли — элемент отображается
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_login_via_personal_account_button(self, logged_in_user, driver):
        """Тест входа через кнопку 'Личный кабинет'."""
        wait = WebDriverWait(driver, 15)

        # Переходим на главную
        driver.get(BASE_URL)

        # Нажимаем "Личный кабинет"
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Заполняем форму
        email, password, name = logged_in_user
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли — элемент отображается
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_login_via_registration_form(self, logged_in_user, driver):
        """Тест входа через ссылку 'Войти' на странице регистрации."""
        wait = WebDriverWait(driver, 15)

        # Переходим на страницу регистрации
        driver.get(REGISTER_URL)

        # Нажимаем ссылку "Войти"
        wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()

        # Заполняем форму
        email, password, name = logged_in_user
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли — элемент отображается
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_login_via_password_recovery_form(self, logged_in_user, driver):
        """Тест входа через ссылку 'Войти' на странице восстановления пароля."""
        wait = WebDriverWait(driver, 15)

        # Переходим на страницу восстановления пароля
        driver.get(FORGOT_PASSWORD_URL)

        # Нажимаем ссылку "Войти"
        wait.until(EC.element_to_be_clickable(RestorePasswordPageLocators.LOGIN_LINK))
        driver.find_element(*RestorePasswordPageLocators.LOGIN_LINK).click()

        # Заполняем форму
        email, password, name = logged_in_user
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли — элемент отображается
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()
