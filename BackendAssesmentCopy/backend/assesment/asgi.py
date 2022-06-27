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
import app.schemas as schemas
from app import models
import utils.consumer as consumer 
import utils.dbmanagers.crud as crud 


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Converting json data to python class object
def jsonObjDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Tenant':
        data=models.Tenant(obj['tenant_id'], obj['tenant_name'], obj['address'], obj['city'], obj['state'], obj['country'], obj['zip_code'], obj['phone'], obj['web_url'])	
    if '__type__' in obj and obj['__type__'] == 'User':
        data=models.User(obj['user_id'], obj['first_name'], obj['last_name'], obj['department'], obj['designation'], obj['tenant_id'], obj['city'], obj['country'], obj['bio'], obj['social_links'], obj['employee_id'])
    return data

#Inserting data into consumer database   	
def FuncTwo(db: Session = Depends(get_db)):
    print('Consumer Started:', flush=True)	
    m=consumer.consume_events()
    classObj = json.loads(m,object_hook=jsonObjDecoder)
    className = (type(classObj).__name__)
    if className == 'Tenant':
        classObj = crud.get_tenant_by_id(db, tenant_id=classObj.tenant_id)
        if classObj:
             raise HTTPException(status_code=400, detail="Record already exists")
        try:
            crud.create_tenant(db=db, tenant=classObj)
        except Exception as error:
             print(error, flush=True)
    if className == 'User':
         classObj = crud.get_user_by_id(db, user_id=classObj.user_id)
         if classObj:
              raise HTTPException(status_code=400, detail="Record already exists")
         try:
             crud.create_user(db=db, user=classObj)
         except Exception as error:
              print(error, flush=True)
    
if __name__ == "__main__":
    thread_one = Thread(target=FuncTwo,daemon=True)
    thread_one.start()
    uvicorn.run(app, host="0.0.0.0", port=5020)





