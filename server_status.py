from selenium import webdriver
import time
from bs4 import BeautifulSoup

def parse_page(driver):
    # 페이지 소스 가져오기
    page_source = driver.page_source
    # BeautifulSoup을 사용하여 페이지 파싱
    soup = BeautifulSoup(page_source, "html.parser")

    cs_country_id = ['south_korea', 'japan', 'hong_kong', 'china_shanghai']
    cs_country_id_base = 'csgo_'
    cs_class_check = ['good', 'minor']
    cs_class_base = 'status '
    server_statuses = {}  # 서버 상태를 저장할 딕셔너리
    #status_element = soup.find("span", class_="status minor", id="csgo_japan")

    status_element = None

    for country_id in cs_country_id:
        status_element = None

        for cs_class in cs_class_check:
            check = soup.find("span",
                              class_=cs_class_base + cs_class,
                              id=cs_country_id_base + country_id)
            if check is not None:
                status_element = check.text.strip()
                break

        if status_element is not None:
            server_statuses[country_id] = status_element

    return server_statuses

    #print(status_element)
    if status_element is not None:
        # 요소의 텍스트 가져오기
        status_text = status_element
        #print(status_text)
        return status_text

    #return None

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