from importlib.machinery import all_suffixes
import json
from json import loads
from sys import api_version
from kafka import KafkaConsumer
from kafka import KafkaProducer
import asyncio
import os
from app import schemas
from app import routes
from app.schemas import TenantBase, TenantCreate, Tenant, UserBase, UserCreate, User
from app import models
from app.config import Base, SessionLocal, engine
from sqlalchemy.orm import Session
import utils.dbmanagers.crud as crud 
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Response

TOPIC_NAME = 'data_topic'

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
consumer = KafkaConsumer(TOPIC_NAME,auto_offset_reset='latest',bootstrap_servers='kafkatwo:9092',value_deserializer=lambda msg: loads(msg.decode('utf-8')))

def consume_events(db: Session = Depends(get_db)):
    for m in consumer:
        print("testing", flush=True)
        print(m, m.value, type(m.value), flush=True)
        print(m.value["properties"], flush=True)
        if(m.value["event"] == 'tenant_created'):
            tenant_one = TenantCreate(**m.value["properties"])
            try:
                print(type(tenant_one),flush=True)
                db=get_db()
                new_db=next(db)
                crud.create_tenant(new_db,tenant_one)
            except Exception as error:
                print(error,flush=True)
        if(m.value["event"] == 'user_created'):
            user_one = UserCreate(**m.value["properties"])
            try:
                print(type(user_one),flush=True)
                db=get_db()
                new_db=next(db)
                crud.create_user(new_db,user_one)
            except Exception as error:
                print(error,flush=True)

        


        

        