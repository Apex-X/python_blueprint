from fastapi import FastAPI
from .handlers import example


http_server = FastAPI()

http_server.include_router(example.router, prefix="/test")
