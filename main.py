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