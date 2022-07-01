#from app.schemas import TenantBase
#from assesment.app.schemas import TenantBase
#from backend.assesment.app.schemas import Tenant
import uvicorn
import pydantic
import sys
import asyncio
import threading
import json
from threading import Thread
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Response
from app.config import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from app.main import app
from app import schemas
from app import models
from app.schemas import TenantBase, TenantCreate, Tenant
import utils.consumer as consumer 
import utils.dbmanagers.crud as crud 

#Inserting data into consumer database   	
def FuncTwo():
    print('Consumer Started:', flush=True)	
    consumer.consume_events()
        
if __name__ == "__main__":
    thread_one = Thread(target=FuncTwo,daemon=True)
    thread_one.start()
    uvicorn.run(app, host="0.0.0.0", port=5020)





