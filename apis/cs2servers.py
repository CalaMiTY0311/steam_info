import requests
from fastapi import APIRouter
from dotenv import load_dotenv
import os

from pprint import pprint

cs2status = APIRouter()

load_dotenv()
api_key = os.environ.get('api_key')

@cs2status.get("/cs2servers")
def status():
    url = f"https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key={api_key}"
    response = requests.get(url)
    response = response.json()['result']

    # datacenters
    centers = response['datacenters']


    matchmaking_info = response['matchmaking']
    
    

    return response
