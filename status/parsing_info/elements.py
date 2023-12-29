from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from server_info import server_status

def elements(wait):
    server = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "regions")))
    onlines = wait.until(EC.presence_of_all_elements_located((By.ID, "online")))
    ingames = wait.until(EC.presence_of_all_elements_located((By.ID, "ingame")))
    # server_status(server)

    result = {}
    result['server'] = server_status(server)
    result['users'] = steam_users_num(wait)
    return result

    return server, onlines, ingames