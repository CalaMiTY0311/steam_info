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

info = info['result']