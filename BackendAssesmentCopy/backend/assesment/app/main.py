import uvicorn
from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# import crud, models, schemas #ERROR
from .config import Base, SessionLocal, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
