# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# from server_info import server_status
# from server_users_info import steam_users_num

# from steam_info.status.chrome.driver import on_chrome

def elements(wait):

    server = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "regions")))
    onlines = wait.until(EC.presence_of_all_elements_located((By.ID, "online")))
    ingames = wait.until(EC.presence_of_all_elements_located((By.ID, "ingame")))

    return server , onlines , ingames

