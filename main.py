from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse

# from status.cm_status import parse_page

import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from status.cm_status import parse_page

@app.get("/status")
async def get_status():
    result = parse_page()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")