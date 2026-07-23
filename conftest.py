import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from helpers import generate_email, generate_password, generate_name
from constants import REGISTER_URL


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def firefox_driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user(driver):
    """Фикстура: регистрация нового пользователя. Возвращает (email, password, name)."""
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
    return email, password, name


@pytest.fixture
def logged_in_user(registered_user, driver):
    """Фикстура: регистрация + вход. Возвращает (email, password, name)."""
    email, password, name = registered_user
    wait = WebDriverWait(driver, 15)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
    return email, password, name
