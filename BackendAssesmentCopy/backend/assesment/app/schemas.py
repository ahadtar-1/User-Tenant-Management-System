from typing import List, Optional, Dict

from pydantic import BaseModel

class TenantBase(BaseModel):
    tenant_id: int
    tenant_name: str
    address: str
    city: str
    state: str
    country: str
    zip_code: str
    phone: str
    web_url: str

class TenantCreate(TenantBase):
    pass

    class Config:
        orm_mode = True

class Tenant(TenantBase):
    pass

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    department: str
    designation: str
    tenant_id: int
    city: str
    country: str
    bio: str
    social_links: str
    employee_id: int

class UserCreate(UserBase):
    pass

    class Config:
        orm_mode = True

class User(UserBase):
    pass

    class Config:
        orm_mode = True