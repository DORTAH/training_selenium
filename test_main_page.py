from main_page import MainPage

def test_guest_can_see_login_lik(browser):
    page = MainPage(browser, "http://10.11.16.134")
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://10.11.16.134")
    page.open()
    page.go_to_login_page()