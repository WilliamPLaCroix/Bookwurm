# .venv\Scripts\Activate.ps1

from fastapi import FastAPI
from typing import Annotated

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

