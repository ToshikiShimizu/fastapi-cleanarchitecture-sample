from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.api import exception_handlers
from app.api.routers import item_router

app = FastAPI()

app.include_router(item_router.router)

app.add_exception_handler(
    HTTPException, exception_handlers.http_exception_handler)
