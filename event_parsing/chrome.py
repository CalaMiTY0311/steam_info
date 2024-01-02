from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

def on_chrome():

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(
    #     # options=options, 
    #     service=service)
    driver = webdriver.Chrome(
         )
    # stealth(driver,        
    #         languages=["en-US", "en"],        
    #         vendor="Google Inc.",        
    #         platform="Win32",        
    #         webgl_vendor="Intel Inc.",        
    #         renderer="Intel Iris OpenGL Engine",       
    #         fix_hairline=True,       
    #         )

    url = "https://steambase.io/sales"

    driver.get(url)

    wait = WebDriverWait(driver, 30)
    time.sleep(1)
    return wait
