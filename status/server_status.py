from selenium import webdriver
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

    wait = WebDriverWait(driver, 2)
    time.sleep(1)


    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "regions")))

    result = {}
    regions_list = ['Europe','Americas','Asia','Rest of world']

    for region, element in zip(regions_list, elements):
        lines = element.text.split('\n')
        status={}
        for i in range(0, len(lines), 3):

            regions = list(lines[i].split(' '))
            regions_code = regions[0]
            regions_name = ' '.join(regions[1:])

            status_values = lines[i + 1:i + 3]
            status[regions_code] = {regions_name: status_values}
        
        result[region] = status
        
            
    return result

from pprint import pprint
pprint(status_parser())