# main.py

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from steam_parser import parse_page, reload_page

import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 초기 페이지 로딩
initial_status = parse_page()

def startup_event():
    # 백그라운드 작업으로 주기적으로 페이지를 리로드하는 함수 실행
    background_tasks = BackgroundTasks()
    background_tasks.add_task(reload_page, background_tasks)
    background_tasks.add_task(set_current_status, initial_status)
    return background_tasks  # 수정된 부분

async def set_current_status(current_status):
    # 초기 상태를 설정하는 함수 (예를 들어, 데이터베이스에 저장하는 등의 작업 수행 가능)
    print("Setting initial status:", current_status)

app.add_event_handler("startup", startup_event)

@app.get("/status")
async def get_status():
    time.sleep(5)
    return JSONResponse(content=initial_status)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")