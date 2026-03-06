import time
import math

# надо для управления браузером
from selenium import webdriver
# класс By содержит способы поиска элементов в DOM странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(5)

# метод get открывает через браузер сайт по url
# driver.get("https://suninjuly.github.io/huge_form.html")
# time.sleep(1)

# find_element ищет элемент на сайте через способы поиска и значения способа
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
#
# # вводит в элемент input текст
# textarea.send_keys("get()")
# time.sleep(1)

# driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000 ))).click()
#
#
# input_name = driver.find_element(By.NAME, "first_name")
# input_last_name = driver.find_element(By.NAME, "last_name")
# city = driver.find_element(By.NAME, "firstname")
# country = driver.find_element(By.ID, "country")
#
# submit_button = driver.find_element(By., "btn")
#
# input_name.send_keys("GOYDA")
# input_last_name.send_keys("GOYDA")
# city.send_keys("GOYDA")
# country.send_keys("GOYDA")


# submit_button.click()

# time.sleep(1)

try:
    wait = WebDriverWait(driver, 15)
    driver.get("https://suninjuly.github.io/explicit_wait2")

    # driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    # driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    # driver.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    # driver.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
    # driver.find_element(By.XPATH, "//input[@placeholder='Input your address:']")

    # for inputEl in driver.find_elements(By.XPATH, "//input[@required]"):
    #     inputEl.send_keys("GOYDA")

    # x = driver.find_element(By.CSS_SELECTOR, ).text
    # driver.find_element(By.ID, "answer" ).send_keys(
    #     str(math.log(abs(12*math.sin(int(x)))))
    # )

    # driver.find_element(By.ID, "robotCheckbox").click()
    # driver.find_element(By.ID, "robotsRule").click()
    #
    # submit_button = driver.find_element(By.CLASS_NAME, "btn")
    # submit_button.click()
    # driver.find_element(By.XPATH, "//input[@placeholder='Input your email'")
    # driver.find_element(By.XPATH, "//input[@required]").click()

    # welcome_text = driver.find_element(By.CSS_SELECTOR, "h1").text
    # assert welcome_text == "Congratulations! You have successfully registered!"


    # driver.find_element(By.CLASS_NAME, "trollface").click()
    #
    #
    # driver.switch_to.window(driver.window_handles[1])
    #
    # x = driver.find_element(By.ID, "input_value").text
    # driver.find_element(By.ID, "answer" ).send_keys(
    #     str(math.log(abs(12*math.sin(int(x)))))
    # )
    #
    # driver.find_element(By.CLASS_NAME, "btn").click()

    # wait.until(EC.element_to_be_clickable((By.ID, "verify")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    driver.find_element(By.ID, "book").click()

    # text = driver.find_element(By.ID, "verify_message").text
    # assert "Verification was successful!" == text

    x = driver.find_element(By.ID, "input_value").text
    driver.find_element(By.ID, "answer" ).send_keys(
        str(math.log(abs(12*math.sin(int(x)))))
    )
    driver.find_element(By.ID, "solve").click()
finally:
    time.sleep(3)
    driver.quit()

# в идеале выполнять это после каждой проверки. заркывает браузер
# driver.quit()
