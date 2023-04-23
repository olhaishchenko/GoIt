from datetime import date

from pydantic import BaseModel, Field, EmailStr

from src.database.models import Role


class ContactModel(BaseModel):
    first_name: str = Field("Katya", max_length=40)
    last_name: str = Field("Bond", max_length=40)
    email: EmailStr
    telephone_number: str = Field("0954567788", max_length=20)
    date_of_birthday: date


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    telephone_number: str
    date_of_birthday: date

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=12)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    avatar: str
    roles: Role

    class Config:
        orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr