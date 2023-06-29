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
                     'tia'
                     ]
    
    cm_class_check = ['good', 'muted']
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
#____________________________________________________________________

    # if cm_status_element is not None:
    #     cm_status_element = cm_status_element.text.strip()
    #     print(cm_status_element)
    # else:
    #     print("N/A")
    
#--------------------------------------cs server-----------------------------------------------
    cs_country_id = [
                     'south_korea', 
                     'japan', 
                     'hong_kong', 
                     'china_guangzhou', 
                     'china_shanghai', 
                     'china_tianjin'
                     ]
    
    cs_country_id_base = 'csgo_'
    cs_class_check = ['good', 'minor']
    cs_class_base = 'status '
    cs_server_statuses = {}  # 서버 상태를 저장할 딕셔너리
    #cs_status_element = soup.find("span", class_="status minor", id="csgo_japan")

    cs_status_element = None

    for country_id in cs_country_id:
        cs_status_element = None

        for cs_class in cs_class_check:
            check = soup.find("span",
                              class_=cs_class_base + cs_class,
                              id=cs_country_id_base + country_id)
            if check is not None:
                cs_status_element = check.text.strip()
                break

        if cs_status_element is not None:
            cs_server_statuses[country_id] = cs_status_element
#--------------------------------------cs server-----------------------------------------------
    return cs_server_statuses, cm_server_statuses

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