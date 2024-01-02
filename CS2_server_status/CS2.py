import requests

def CS2_server(api_key):
    url = f"https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1/?key={api_key}"
    response = requests.get(url)
    info = response.json()
    return info
