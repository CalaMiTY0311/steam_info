# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def steam_users_num(wait):

    onlines = wait.until(EC.presence_of_all_elements_located((By.ID, "online")))
    ingames = wait.until(EC.presence_of_all_elements_located((By.ID, "ingame")))

    online_ingame = []
    for online in onlines:
        online_ingame.append(online.text)
    for ingame in ingames:
        online_ingame.append(ingame.text)

    return online_ingame
        