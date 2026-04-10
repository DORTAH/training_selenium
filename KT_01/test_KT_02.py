import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
import random
import string

from selenium.webdriver.chrome.options import Options
fake = Faker('ru_RU')

password = fake.password()

url_reg = "https://chipollino-sad.ru/auth/registration/"
url_sign_in = "https://chipollino-sad.ru/auth/"


class TestRegisterPage:

    @pytest.mark.reg
    def test_register(self, browser):
        browser.get(url_reg)
        browser.find_element(By.NAME, "REGISTER[EMAIL]").send_keys(fake.email())
        browser.find_element(By.NAME, "REGISTER[LAST_NAME]").send_keys(fake.last_name())
        browser.find_element(By.NAME, "REGISTER[NAME]").send_keys(fake.first_name())
        browser.find_element(By.NAME, "REGISTER[PASSWORD]").send_keys(password)
        browser.find_element(By.NAME, "REGISTER[CONFIRM_PASSWORD]").send_keys(password)
        browser.find_element(By.ID, "nca-cookiesaccept-line-accept-btn").click()
        browser.find_element(By.XPATH, "//input[@value='Регистрация']").click()

        try:
            welcome_element = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.auth-form-box.auth-form p"))
            )
        except TimeoutException:
            assert False, "Зарегаться не получилось("

    @pytest.mark.login
    def test_login_in(self, browser):
        browser.get(url_sign_in)
        wait = WebDriverWait(browser, 5)

        wait.until(EC.element_to_be_clickable((By.ID, "closeModalBtn"))).click()

        user_login = "testessrtre@gmail.com"
        user_pass = "find_element"
        browser.find_element(By.NAME, "USER_LOGIN").send_keys(user_login)
        browser.find_element(By.NAME, "USER_PASSWORD").send_keys(user_pass)
        browser.find_element(By.ID, "nca-cookiesaccept-line-accept-btn").click()
        browser.find_element(By.XPATH, "//input[@value='Войти']").click()

        try:
            sign_in_tru = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sale-personal-section-index-block"))
            )
        except TimeoutException:
            assert False, "Войти не получилось"

        browser.find_element(By.CLASS_NAME, "top-logo").click()
        browser.find_element(By.XPATH, "//a[@href='/new/']").click()

        item_name = browser.find_element(By.CSS_SELECTOR, "div.product_item_title a").text.strip()
        item_price = browser.find_element(By.CSS_SELECTOR, "div.product-item-price-current span").text.strip()
        browser.find_element(By.CLASS_NAME, "btn-buy").click()
        browser.find_element(By.CLASS_NAME, "basket-icon").click()
        try:
            cart_name = browser.find_element(By.CSS_SELECTOR, "img.basket-item-image").get_attribute("alt").strip()

            assert item_name == cart_name, "Название не то"

            cart_price = browser.find_element(By.CSS_SELECTOR, "span.basket-item-price-current-text").text.strip()

            assert cart_price == item_price, "Цена не та"
            browser.find_element(By.CLASS_NAME, "clear_basket").click()
        except AssertionError:
            print("Что-то хрень какаято")

    @pytest.mark.login
    @pytest.mark.parametrize("username, passwordes", [
        ("testessrtre@gmail.com","find_element"),
        ("testessrtre2@gmail.com","find_element"),
        ("testessrtre3@gmail.com","find_element")
    ])
    def test_login(self, browser, username, passwordes):


        browser.get(url_sign_in)
        wait = WebDriverWait(browser, 5)

        wait.until(EC.element_to_be_clickable((By.ID, "closeModalBtn"))).click()


        browser.find_element(By.NAME, "USER_LOGIN").send_keys(username)
        browser.find_element(By.NAME, "USER_PASSWORD").send_keys(passwordes)
        browser.find_element(By.ID, "nca-cookiesaccept-line-accept-btn").click()
        browser.find_element(By.XPATH, "//input[@value='Войти']").click()

        try:
            sign_in_tru = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "sale-personal-section-index-block"))
            )
        except TimeoutException:
            assert False, f"Войти не получилось {username} {passwordes}"

