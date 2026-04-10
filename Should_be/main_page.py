from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(By.ID, "login_link").click()

    def should_be_login_link(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#loggin_link_invalid"), "Не нашли ссылку на вход"

"""
1) Открыть страницу товара
2) Нажать кнопку добавить в корзину
3) Посчитать результат математического выражения и отправить его в alert, а так же print

Результат:
1) Сообщение о том, что товар добавлен в корзину. Название товара должно совпадать с тен товарон, который
•добавили
2) Сообщение со стоимостью корзины. Стоимость корзины должна совпвдвть с товаром 
"""