from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

import time

def on_chrome():
    
    # service = Service(executable_path=ChromeDriverManager().install())

    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    
    driver = webdriver.Chrome(
        # options=options
        )

    url = "https://steamstat.us/"

    driver.get(url)

    wait = WebDriverWait(driver, 2)
    time.sleep(1)
    return wait