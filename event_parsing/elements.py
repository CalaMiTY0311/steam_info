from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from chrome import on_chrome

wait = on_chrome()
sale_name = wait.until(EC.presence_of_all_elements_located((By.ID, "hero")))
for i in sale_name:
    print(i.text)

