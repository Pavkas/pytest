from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    input_registration_email = (By.CSS_SELECTOR, "#id_registration-email")
    input_registration_password_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    input_registration_password_2 = (By.CSS_SELECTOR, "#id_registration-password2")

    input_login_email = (By.CSS_SELECTOR, "#id_login-username")
    input_login_password = (By.CSS_SELECTOR, "#id_login-password")

