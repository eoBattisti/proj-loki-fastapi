from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
import logging
from multiprocessing import Queue
from logging_loki import LokiQueueHandler


app = FastAPI()

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.handlers = gunicorn_error_logger.handlers
fastapi_logger.setLevel(gunicorn_logger.level)

loki_handler = LokiQueueHandler(
    Queue(-1),
    url="http://loki:3100/loki/api/v1/push", 
    tags={"application": "fastapi-app"},
    version="1",
)
fastapi_logger.addHandler(loki_handler)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "value": f"Item {item_id}"}
