from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str

    class Collection:
        name = "admin"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Prabaharan",
                "email": "prabaharan.auroville@gmail.com",
                "password": "stemland"
            }
        }


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "prabaharan.auroville@gmail.com",
                "password": "stemland"
            }
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "prabaharan",
                "email": "prabaharan.auroville@gmail.com",
            }
        }
