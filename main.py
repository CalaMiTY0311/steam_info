from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

from apis.cs2servers import cs2status

import dotenv

import time

app = FastAPI()
app.include_router(cs2status)

@app.get("/")
def read_root():
    return {"Hello": "World"}

#steamstat.us에서 CM과 CS2 서버 상태를 파싱해오는 코드 (밑에 주석만 해제하면 postman으로 조회가능)
# #--------------------------------------------------------------------- parsing steamstat ---------------------------------------------------------------------
# from status_parsing.chrome.driver import on_chrome
# from status_parsing.parsing_info.elements import elements
# from status_parsing.parsing_info.server_info import server_status
# from status_parsing.parsing_info.server_users_info import steam_users_num

# @app.get("/status")
# async def status():
#     wait = on_chrome()
    
#     server,onlines,ingames= elements(wait)
#     result = {}
#     result['users'] = steam_users_num(onlines,ingames)
#     result['server'] = server_status(server)
#     return result
# #--------------------------------------------------------------------- parsing steamstat ---------------------------------------------------------------------

# from steam_info.apis.cs2servers import CS2_server
# from event_parsing.events import sales
# from event_parsing.chrome import on_chrome

# @app.get("/CS2_Server_Status")
# def CS2_Server_Status():
#     try:
#         # dotenv_file = dotenv.find_dotenv()
#         # dotenv.load_dotenv(dotenv_file)
#         # api_key = dotenv.dotenv_values(dotenv_file)['STEAM_WEPAPI_KEY']
#         api_key = os.getenv('STEAM_WEPAPI_KEY')
#         return CS2_server(api_key)
#     except Exception as e:
#         return {"error" : str(e)}


# #
# @app.get("/event_info")
# def event_info():
#     try:
#         wait = on_chrome()
#         result = sales(wait)
#         return result
#     except Exception as e:
#         return {"error" : str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")