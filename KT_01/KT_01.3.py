import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
import random
import string

from selenium.webdriver.chrome.options import Options

fake = Faker('ru_RU')

chrome_options = Options()
chrome_options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(5)



try:
    wait = WebDriverWait(driver, 5)
    driver.get("https://chipollino-sad.ru/auth/")

    wait.until(EC.presence_of_element_located((By.ID, "closeModalBtn"))).click()

    password = fake.password()
    user_login = "testessrtre@gmail.com"
    user_pass = "Не правильно"
    driver.find_element(By.NAME, "USER_LOGIN").send_keys(user_login)
    driver.find_element(By.NAME, "USER_PASSWORD").send_keys(user_pass)
    driver.find_element(By.ID, "nca-cookiesaccept-line-accept-btn").click()
    driver.find_element(By.XPATH, "//input[@value='Войти']").click()

    try:
        sign_in_tru = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(( By.CLASS_NAME, "sale-personal-section-index-block"))
        )
    except TimeoutException:
        assert False, "Войти не получилось"




    # testessrtre@gmail.com
    # Пупкин
    # Пупа
    # find_element
    # find_element
finally:
    time.sleep(5)
    driver.quit()

