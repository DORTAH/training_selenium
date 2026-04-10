from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registration_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Мы похоже не на странице логина"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы логина"

    def should_be_registration_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы регистрации"
