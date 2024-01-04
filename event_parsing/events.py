from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from chrome import on_chrome
from datetime import datetime
import pytz

wait = on_chrome()

result = {} 

#Now or Next sale info
now_sale_check = wait.until(EC.presence_of_all_elements_located((By.ID, "hero")))

for now_sale in now_sale_check:
    elements = now_sale.find_elements(By.XPATH, "//p[@class='text-2xl font-normal !text-slate-300']")

elements = [element.text for element in elements]
elements = elements[0].split('\n')


event_info, YMD = list(elements[0].split(' ')), list(elements[1].split(' '))
event_name = ' '.join(event_info[:event_info.index('is')])


YMD = YMD[-1]
HM = now_sale.find_elements(By.XPATH, "//span[@class='font-light text-slate-400']")
HM=HM[0].text
HM = list(HM.split(' '))
HM = [HM[0].replace('(', ''),HM[1]]

combined_datetime_string = f"{YMD} {HM[0]} {HM[1]}"
combined_datetime = datetime.strptime(combined_datetime_string, "%m/%d/%Y %I:%M %p")

input_timezone = pytz.timezone('America/Los_Angeles')
combined_datetime = input_timezone.localize(combined_datetime)
output_timezone = pytz.timezone('Asia/Seoul')
korean_datetime = combined_datetime.astimezone(output_timezone)

if event_info[-1] == 'live!':
    result['now_event']  = {event_name : korean_datetime}
    result['next_event'] = {}
elif event_info[-1] == 'next':
    result['now_event']  = {}
    result['next_event'] = {event_name : korean_datetime}


#Upcoming sale info
upcoming_sales_check = wait.until(EC.presence_of_all_elements_located((By.ID, "upcoming-sales")))

upcoming_sales_info=[]
for i in upcoming_sales_check:
    lines = i.text.split('\n')
    for line in lines:
        upcoming_sales_info.append(line)
upcoming_sales_info = upcoming_sales_info[2:]
upcoming_sales_info = [upcoming_sales_info[i:i+4] for i in range(0, len(upcoming_sales_info), 5)]

upcoming = []
for lst in upcoming_sales_info:
    result_dict = {
        "event_name": lst[0],
        "event_quality": lst[1],
        "event_start": lst[2],
        "event_end": lst[3],

    }
    upcoming.append(result_dict)

    

