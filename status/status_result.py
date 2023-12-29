from parsing_info.server_info import server_status
from parsing_info.server_users_info import steam_users_num


from chrome.driver import on_chrome

wait = on_chrome()

# def status_list(wait):
#     result = {}
#     result['server'] = server_status(wait)
#     result['users'] = steam_users_num(wait)
#     return result

# print(status_list(wait))