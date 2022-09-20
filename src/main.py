from typing import Union
from routes.router import user

from fastapi import FastAPI

app = FastAPI()

app.include_router(user)