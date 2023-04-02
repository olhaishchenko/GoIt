from datetime import date
from pydantic import BaseModel, Field, EmailStr


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
    phone: str
    birthday: date

    class Config:
        orm_mode = True
