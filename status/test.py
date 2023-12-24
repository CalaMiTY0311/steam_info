from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def on_chrome():
    chrome_driver = webdriver.Chrome()
    return chrome_driver

def status_parser():

    driver = on_chrome()

    url = "https://steamstat.us/"

    driver.get(url)

    wait = WebDriverWait(driver, 5)
    time.sleep(1)

    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "regions")))

    
    info = {}  
    server_container = ['Europe', 'Americas', 'Asia', 'Rest_of_world']

    for server, element in zip(server_container, elements):
        text_without_newline = element.text.replace('\n', ' ')
        info[server] = text_without_newline.split()

    return info

from pprint import pprint
print(status_parser())