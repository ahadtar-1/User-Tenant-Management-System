from fastapi import Depends, FastAPI, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session

from app.config import Base, SessionLocal, engine
import app.schemas as schemas
import app.models as models

import utils.dbmanagers.crud as crud 
import utils.consumer as consumer

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, userid=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Record already exists")   
    crud.create_user(db=db, user=user)
    return "User Inserted"

@router.post("/tenants/", response_model=schemas.Tenant)
def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = crud.get_tenant_by_id(db, tenant_id=tenant.tenant_id)
    if db_tenant:
        raise HTTPException(status_code=400, detail="Record already exists")
    crud.create_tenant(db=db, tenant=tenant)
    return "Tenant Inserted"

@router.get("/users/", response_model=schemas.User)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/tenants/", response_model=schemas.Tenant)
def read_tenants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tenants = crud.get_tenants(db, skip=skip, limit=limit)
    return tenants

@router.get("/tenants/{tenant_id}", response_model=schemas.Tenant)
def read_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_tenant = crud.get_tenant_by_id(db, tenant_id=tenant_id)
    #if db_tenant is None:
        #raise HTTPException(status_code=404, detail="User not found")
    return db_tenant

@router.delete('/users/{user_id}', response_model=schemas.User)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
     db_user = crud.get_user_by_id(db, user_id=user_id)
     if db_user is None:
         raise HTTPException(status_code=404, detail="User not found")
     crud.delete_user(db=db,user_id=user_id)

@router.delete('/tenants/{tenant_id}', response_model=schemas.Tenant)
def delete_tenant_by_id(tenant_id: int, db: Session = Depends(get_db)):
     db_tenant = crud.get_tenant_by_id(db, tenant_id=tenant_id)
     if db_tenant is None:
         raise HTTPException(status_code=404, detail="User not found")
     crud.delete_tenant(db=db,tenant_id=tenant_id)
