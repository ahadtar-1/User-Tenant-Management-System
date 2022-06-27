from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config import Base

class Tenant(Base):
    __tablename__ = "tenants"

    tenant_id = Column(Integer, primary_key=True)
    tenant_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip_code = Column(String)
    phone = Column(String)
    web_url = Column(String)
    


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    department = Column(String)
    designation = Column(String)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    city = Column(String)
    country = Column(String)
    bio = Column(String)
    social_links = Column(String)
    employee_id = Column(Integer)
