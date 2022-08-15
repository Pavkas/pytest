from .base_page import BasePage
from .locators import MainPageLocators
from pages.main_page import MainPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.input_login_email), "login-username is not presented"
        assert self.is_element_present(*MainPageLocators.input_login_password), "login-password is not presented"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators.input_registration_email), "registration-email is not presented"
        assert self.is_element_present(*MainPageLocators.input_registration_password1), "registration-password1 is not presented"
        assert self.is_element_present(*MainPageLocators.input_registration_password2), "registration-password2 is not presented"
