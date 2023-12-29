from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def on_chrome():
    driver = webdriver.Chrome()

    url = "https://steamstat.us/"

    driver.get(url)

    wait = WebDriverWait(driver, 2)
    time.sleep(1)
    return wait