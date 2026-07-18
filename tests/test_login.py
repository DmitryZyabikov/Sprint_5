import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators, RestorePasswordPageLocators
from helpers import generate_email, generate_password, generate_name

# Константы с URL-адресами
BASE_URL = "https://stellarburgers.education-services.ru"
REGISTER_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"


class TestLogin:
    def test_login_via_main_page_button(self, driver):
        # Тест входа через главную страницу
        # Сначала регистрируем пользователя
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        name = generate_name()
        email = generate_email()
        password = generate_password(6)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ждем перехода на страницу входа
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))

        # Переходим на главную
        driver.get(BASE_URL)

        # Нажимаем кнопку "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Заполняем форму
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли (проверяем видимость элемента, а не текст)
        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))

    def test_login_via_personal_account_button(self, driver):
        # Тест входа через личный кабинет
        # Регистрация
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        name = generate_name()
        email = generate_email()
        password = generate_password(6)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))

        # Переходим на главную
        driver.get(BASE_URL)

        # Нажимаем "Личный кабинет"
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Заполняем форму
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли
        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))

    def test_login_via_registration_form(self, driver):
        # Тест входа через форму регистрации
        # Регистрация
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        name = generate_name()
        email = generate_email()
        password = generate_password(6)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))

        # Переходим обратно на регистрацию
        driver.get(REGISTER_URL)

        # Нажимаем ссылку "Войти"
        wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK))
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()

        # Заполняем форму
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли
        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))

    def test_login_via_password_recovery_form(self, driver):
        # Тест входа через форму восстановления пароля
        # Регистрация
        driver.get(REGISTER_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        name = generate_name()
        email = generate_email()
        password = generate_password(6)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))

        # Переходим на страницу восстановления пароля
        driver.get(FORGOT_PASSWORD_URL)

        # Нажимаем ссылку "Войти"
        wait.until(EC.element_to_be_clickable(RestorePasswordPageLocators.LOGIN_LINK))
        driver.find_element(*RestorePasswordPageLocators.LOGIN_LINK).click()

        # Заполняем форму
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        # Проверяем, что вошли
        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))