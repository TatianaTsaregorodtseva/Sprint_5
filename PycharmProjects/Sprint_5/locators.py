from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт"
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Ссылка "Личный кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//a[@href='/account']")
    # Логотип в шапке страницы
    A_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    # Кнопка "Конструктор"
    BUTTON_DESIGNER = (By.CLASS_NAME, "AppHeader_header__link__3D_hX")
    # Кнопка "Оформить заказ"
    BUTTON_CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")
    # Поле ввода "Имя"
    INPUT_NAME = (By.XPATH, "//fieldset[1]//input")
    # Поле ввода "Email" в форме регистрации
    INPUT_EMAIL_R = (By.XPATH, "//fieldset[2]//input")
    # Поле ввода "Пароль" в форме регистрации/входа
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    # Кнопка "Зарегистрироваться" в форме регистрации
    BUTTON_TO_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение о некорректном пароле в форме регистрации
    ERROR_PASSWORD = (By.XPATH, "//p[contains(@*, 'error')]")
    # Ссылка "Войти" в форме регистрации/восстановления пароля
    A_INTER = (By.CLASS_NAME, "Auth_link__1fOlj")
    # Слово "Вход" на странице входа
    WORD_LOGIN = (By.XPATH, "//h2[text()='Вход']")
    # Ссылка "Зарегистрироваться" на странице входа
    A_TO_REGISTER = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Поле ввода "Email" в форме входа
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    # Кнопка "Войти" в форме входа
    BUTTON_INTER = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Восстановить пароль"
    A_RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    # "Профиль" в личном кабинете
    A_PROFILE = (By.XPATH, "//a[text()='Профиль']")
    # Кнопка "Выход" в личном кабинете
    BUTTON_OUT = (By.XPATH, "//button[text()='Выход']")
    # Кнопка "Булки"
    BUTTON_ROLLS = (By.XPATH, "//span[text()='Булки']/..")
    # Кнопка "Соусы"
    BUTTON_SAUCES = (By.XPATH, "//span[text()='Соусы']/..")
    # Кнопка "Начинки"
    BUTTON_STUFFINGS = (By.XPATH, "//span[text()='Начинки']/..")
    # Раздел "Булки"
    SECTION_ROLLS = (By.XPATH, "//h2[text()='Булки']")
    # Раздел "Соусы"
    SECTION_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    # Раздел "Начинки"
    SECTION_STUFFINGS = (By.XPATH, "//h2[text()='Начинки']")