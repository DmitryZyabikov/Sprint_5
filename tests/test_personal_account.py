import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators, RegisterPageLocators
from helpers import generate_email, generate_password, generate_name


class TestPersonalAccount:

    def test_navigate_to_personal_account(self, driver):
        # Тест перехода в личный кабинет
        # Регистрация и вход
        driver.get("https://stellarburgers.education-services.ru/register")
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

        # Входим
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверяем что открылся личный кабинет
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))
        profile_text = driver.find_element(*ProfilePageLocators.PROFILE_DESCRIPTION).text
        assert "В этом разделе" in profile_text

    def test_navigate_from_account_to_constructor(self, driver):
        # Тест перехода в конструктор через кнопку
        # Регистрация и вход
        driver.get("https://stellarburgers.education-services.ru/register")
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

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        # Проверяем что вернулись в конструктор
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))
        assert driver.find_element(*MainPageLocators.BURGER_TITLE).text == "Соберите бургер"

    def test_navigate_from_account_via_logo(self, driver):
        # Тест перехода в конструктор через логотип
        # Регистрация и вход
        driver.get("https://stellarburgers.education-services.ru/register")
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

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем на логотип
        driver.find_element(*MainPageLocators.LOGO).click()

        # Проверяем что вернулись в конструктор
        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))
        assert driver.find_element(*MainPageLocators.BURGER_TITLE).text == "Соберите бургер"

    def test_logout_from_account(self, driver):
        # Тест выхода из аккаунта
        # Регистрация и вход
        driver.get("https://stellarburgers.education-services.ru/register")
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

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(EC.presence_of_element_located(MainPageLocators.BURGER_TITLE))

        # Переходим в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.presence_of_element_located(ProfilePageLocators.PROFILE_DESCRIPTION))

        # Нажимаем кнопку "Выход"
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        # Проверяем что перешли на страницу входа
        wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert driver.find_element(*LoginPageLocators.LOGIN_TITLE).text == "Вход"
