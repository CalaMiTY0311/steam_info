from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def on_chrome():
    
    # chrome_options = Options()
    # # chrome_options = Options()
    # # chrome_options.add_argument('--headless')
    # caps = DesiredCapabilities.CHROME
    # caps["pageLoadStrategy"] = "none"

    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option("useAutomationExtension", False)
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        # options=chrome_options
        # options=chrome_options
        )
    url = "https://steamstat.us/"

    driver.get(url)

    wait = WebDriverWait(driver, 30)
    # driver.implicitly_wait(30)
    time.sleep(1)
    return wait