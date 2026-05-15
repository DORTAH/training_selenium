import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


chrome_options = ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://10.11.19.91:4444",
    options=chrome_options
)

try:
    driver.get("https://google.com")
    driver.find_element(By.NAME, "q").send_keys("Selenium Grid")
finally:
    time.sleep(5)
    driver.quit()