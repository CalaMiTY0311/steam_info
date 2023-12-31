# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def on_chrome():
    
    driver = webdriver.Chrome(
        )

    url = "https://steamstat.us/"

    driver.get(url)

    wait = WebDriverWait(driver, 2)
    time.sleep(1)
    return wait

def status_parser():

    wait = on_chrome()
    onlines = wait.until(EC.presence_of_all_elements_located((By.ID, "online")))
    ingames = wait.until(EC.presence_of_all_elements_located((By.ID, "ingame")))

    online_ingame = []
    for online in onlines:
        online_ingame.append(online.text)
    for ingame in ingames:
        online_ingame.append(ingame.text)

    return list(map(int,online_ingame))

print(status_parser())