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
    driver.get("https://chipollino-sad.ru/auth/registration/")

    wait.until(EC.presence_of_element_located((By.ID, "closeModalBtn"))).click()

    password = fake.password()
    driver.find_element(By.NAME, "REGISTER[EMAIL]").send_keys(fake.email())
    driver.find_element(By.NAME, "REGISTER[LAST_NAME]").send_keys(fake.last_name())
    driver.find_element(By.NAME, "REGISTER[NAME]").send_keys(fake.first_name())
    driver.find_element(By.NAME, "REGISTER[PASSWORD]").send_keys(password)
    driver.find_element(By.NAME, "REGISTER[CONFIRM_PASSWORD]").send_keys(password)
    # driver.find_element(By.CLASS_NAME, "agree").click()
    # driver.find_element(By.CLASS_NAME, "agree2").click()
    driver.find_element(By.ID, "nca-cookiesaccept-line-accept-btn").click()
    driver.find_element(By.XPATH, "//input[@value='Регистрация']").click()

    try:
        welcome_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.auth-form-box.auth-form p"))
    )
    except TimeoutException:
        assert False, "Зарегаться не получилось("



    # driver.find_element(By.CLASS_NAME, "top-logo").click()
    # driver.find_element(By.XPATH, "//a[@href='/new/']").click()
    # driver.find_element(By.CLASS_NAME, "btn-buy").click()
    # driver.find_element(By.CLASS_NAME, "basket-icon").click()



finally:
    time.sleep(5)
    driver.quit()

