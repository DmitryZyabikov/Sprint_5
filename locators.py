from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Заголовок "Соберите бургер"
    BURGER_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")


class LoginPageLocators:
    # Заголовок страницы "Вход"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")

    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка "Войти"
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")

    # Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")


class RegisterPageLocators:
    # Заголовок страницы "Регистрация"
    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")

    # Поле ввода Имя
    NAME_INPUT = (By.NAME, "name")

    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']/following::input[1]")

    # Поле ввода Пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Сообщение об ошибке "Некорректный пароль"
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


class RestorePasswordPageLocators:
    # Заголовок страницы "Восстановление пароля"
    RESTORE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")

    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class ProfilePageLocators:
    # Заголовок "В этом разделе вы можете изменить свои персональные данные"
    PROFILE_DESCRIPTION = (By.XPATH, "//p[contains(text(), 'В этом разделе')]")

    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Поле профиля
    PROFILE_SECTION = (By.XPATH, "//a[contains(@class, 'Account_link')]")


class ConstructorLocators:
    # Вкладка "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")

    # Вкладка "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")

    # Вкладка "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    # Активная вкладка (с классом tab_tab_type_current)
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Заголовок секции "Булки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")

    # Заголовок секции "Соусы"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")

    # Заголовок секции "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
