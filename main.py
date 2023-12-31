from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

# from status.cm_status import parse_page

import time



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from status.chrome.driver import on_chrome
from status.parsing_info.elements import elements
from status.parsing_info.server_info import server_status
from status.parsing_info.server_users_info import steam_users_num

@app.get("/status")
async def get_status():
    wait = on_chrome()
    server,onlines,ingames= elements(wait)
    result = {}
    result['users'] = steam_users_num(onlines,ingames)
    result['server'] = server_status(server)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")