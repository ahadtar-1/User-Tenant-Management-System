from sqlalchemy import Integer
from sqlalchemy.orm import Session

from app import models, schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_tenant_by_id(db: Session, tenant_id: int):
    return db.query(models.Tenant).filter(models.Tenant.tenant_id == tenant_id).first()

def get_tenants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tenant).offset(skip).limit(limit).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_tenant(db: Session, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(tenant_id=tenant.tenant_id, tenant_name=tenant.tenant_name, address=tenant.address, city=tenant.city, state=tenant.state, country=tenant.country, zip_code=tenant.zip_code, phone=tenant.phone, web_url=tenant.web_url)
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(user_id=user.user_id, first_name=user.first_name, last_name=user.last_name, department=user.department, designation=user.designation, tenant_id=user.tenant_id, city=user.city, country=user.country, bio=user.bio, social_links=user.social_links, employee_id=user.employee_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_tenant(db: Session, tenant_id: int):
    record = db.query(models.Tenant).filter_by(tenant_id=tenant_id).first()
    db.delete(record)
    db.commit()

def delete_user(db: Session, user_id: int):
    record = db.query(models.User).filter_by(user_id=user_id).first()
    db.delete(record)
    db.commit()

def update_tenant(db: Session,store_data):
    db.merge(store_data)
    db.commit()