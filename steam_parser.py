# test.py

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

def parse_page():
    global driver  

    for _ in range(2):  

        driver.get("https://steamstat.us/")

        driver.implicitly_wait(5)

        page_source = driver.page_source

        soup = BeautifulSoup(page_source, "html.parser")

        cm_country_id = [
            'seo', 'tyo', 'hkg', 'gua', 'sha', 'tia', 'chd'
        ]

        cm_class_check = ['good', 'muted', 'minor']
        cm_class_base = 'status '

        cm_server_statuses = {}

        for country_id in cm_country_id:
            cm_status_element = None

            for cm_class in cm_class_check:
                check = soup.find("span", class_=cm_class_base + cm_class, id=country_id)
                if check is not None:
                    cm_status_element = check.text.strip()
                    break

            if cm_status_element is not None:
                cm_server_statuses[country_id] = cm_status_element
            else:
                cm_server_statuses[country_id] = "N/A"

        if all(status != "N/A" for status in cm_server_statuses.values()):
            return cm_server_statuses

        time.sleep(10)

    return cm_server_statuses

def reload_page(background_tasks, max_retry=3):
    current_retry = 0
    while current_retry <= max_retry:
        current_status = parse_page()
        
        if all(status != "N/A" for status in current_status.values()):
            background_tasks.add_task(set_current_status, current_status)
            break

        current_retry += 1
        print(f"Retrying ({current_retry}/{max_retry})...")
        time.sleep(60)

def set_current_status(current_status):
    print("Setting current status:", current_status)