from base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), f"Нет элемента ссылки на логин"


"""
1) Открыть страницу товара http://10.11.30.32/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear
2) Нажать кнопку добавить в корзину
3) Посчитать результат математического выражения и отправить его в alert, а так же print

Результат:
1) Сообщение о том, что товар добавлен в корзину. Название товара должно совпадать с тем товаром, который добавили
2) Сообщение со стоимостью корзины. Стоимость корзины должно совпадать с товаром
"""