from login_page import LoginPage
from main_page import MainPage

def test_guest_can_see_login_lik(browser):
    link = "http://10.11.30.32"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = Login_page(browser, browser.current_url)
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = MainPage(browser, "http://10.11.16.134")
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()