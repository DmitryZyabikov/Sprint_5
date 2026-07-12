import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Запуск браузера Chrome
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def firefox_driver():
    # Запуск браузера Firefox
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
