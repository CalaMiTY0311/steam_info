from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

# from status.cm_status import parse_page

import time



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from status.chrome.driver import on_chrome
from status.server_status import status_parser

@app.get("/status")
async def get_status():
    wait = on_chrome()
    result = status_parser(wait)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")