from fastapi import FastAPI
from app.api import exception_handlers
from app.api.routers import item_router
from fastapi.exceptions import HTTPException

app = FastAPI()

app.include_router(item_router.router)

app.add_exception_handler(HTTPException, exception_handlers.http_exception_handler)