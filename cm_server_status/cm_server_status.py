from selenium import webdriver
import time
from bs4 import BeautifulSoup


def parse_page(driver):
    # 페이지 소스 가져오기
    page_source = driver.page_source
    # BeautifulSoup을 사용하여 페이지 파싱
    soup = BeautifulSoup(page_source, "html.parser")

    cm_country_id = [
                     'seo', 
                     'tyo', 
                     'hkg', 
                     'gua', 
                     'sha', 
                     'tia',
                     'chd'
                     ]
    
    cm_class_check = ['good', 'muted','minor']
    cm_class_base = 'status '
    #cm_NA_checker = 'No servers in this location'
    #cm_status_element = soup.find("span", class_=cm_class_base + cm_class_check[0], id=cm_country_id[0])
    cm_server_statuses = {}
    #print(cm_status_element)

    for country_id in cm_country_id:
        cm_status_element = None

        for cm_class in cm_class_check:
            check = soup.find("span",
                              class_=cm_class_base + cm_class,
                              id=country_id)
            if check is not None:
                cm_status_element = check.text.strip()
                break

        if cm_status_element is not None:
            cm_server_statuses[country_id] = cm_status_element
        else:
            cm_server_statuses[country_id] = "N/A"
    return cm_server_statuses


# Selenium 웹 드라이버 설정
driver = webdriver.Chrome()  # Chrome 드라이버 사용
driver.get("https://steamstat.us/")  # steamstat.us 페이지 열기

# 이전 값 초기화
previous_status = None

while True:
    driver.refresh()

    # 페이지가 로드될 때까지 기다림
    driver.implicitly_wait(10)

    # 페이지 파싱 및 정보 가져오기
    current_status = parse_page(driver)

    if current_status:
        if current_status != previous_status:
            print("Status changed to:", current_status)
            previous_status = current_status
        else:
            print("Status:", current_status)

    time.sleep(5)

driver.quit()