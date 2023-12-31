from parsing_info.elements import elements
from parsing_info.server_info import server_status
from parsing_info.server_users_info import steam_users_num

from chrome.driver import on_chrome

wait = on_chrome()

server,onlines,ingames= elements(wait)

def parsing_result(server,onlines,ingames):
    result = {}
    result['users'] = steam_users_num(onlines,ingames)
    result['server'] = server_status(server)
    return result

from pprint import pprint
pprint(parsing_result(server,onlines,ingames))