import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from helpers import generate_email, generate_password, generate_name


class TestRegistration:

    def test_successful_registration(self, driver):
        # Тест успешной регистрации
        driver.get("https://stellarburgers.education-services.ru/register")

        wait = WebDriverWait(driver, 15)

        # Ждем загрузку формы
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        # Создаем данные для регистрации
        name = generate_name()
        email = generate_email()
        password = generate_password(6)

        # Заполняем форму
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        # Нажимаем кнопку регистрации
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Проверяем что перешли на страницу входа
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert driver.find_element(*LoginPageLocators.LOGIN_TITLE).text == "Вход"

    def test_registration_with_short_password(self, driver):
        # Тест ошибки при коротком пароле
        driver.get("https://stellarburgers.education-services.ru/register")

        wait = WebDriverWait(driver, 15)

        # Ждем загрузку
        wait.until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT))

        # Создаем данные с коротким паролем
        name = generate_name()
        email = generate_email()
        short_password = generate_password(5)

        # Заполняем форму
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)

        # Нажимаем кнопку
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Проверяем что показалась ошибка
        error_message = wait.until(EC.presence_of_element_located(RegisterPageLocators.PASSWORD_ERROR))
        assert error_message.text == "Некорректный пароль"
