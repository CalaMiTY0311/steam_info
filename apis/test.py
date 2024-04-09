from dotenv import load_dotenv
import requests
import os

# cs2status = APIRouter()

load_dotenv()
api_key = os.environ.get('api_key')
url = f"https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key={api_key}"
response = requests.get(url)
info = response.json()

from pprint import pprint

info = info['result']['datacenters']
# pprint(info)
Europe = {}
Americas = {}
Asia = {}
Remain = {}

for country in info:
    # Europe
    if country.startswith('EU'):
        Europe[country] = info[country]
    # Americas
    elif country.startswith('US'):
        Americas[country] = info[country]
    # Asia
    elif country.startswith('China') or country.startswith('India'):
        Asia[country] = info[country]
    else:
        Remain[country] = info[country]

# pprint(Europe)
# pprint(Americas)
# pprint(Asia)
pprint(Remain)

# import requests
# from bs4 import BeautifulSoup

# def get_steam_sales():
#     url = 'https://store.steampowered.com/news/group/4145017'
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         sale_items = soup.find_all('div', class_='sale')
        
#         pprint(soup)
#     else:
#         print("Failed to retrieve Steam sales data")

# if __name__ == "__main__":
#     get_steam_sales()
