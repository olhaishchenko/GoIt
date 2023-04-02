from datetime import datetime, timedelta, date

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(limit: int, offset: int, db: Session):
    contacts = db.query(Contact).limit(limit).offset(offset).all()
    return contacts


async def get_contact_by_id(contact_id: int, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_contacts_by_first_name(first_name: str, db: Session):
    contact = db.query(Contact).filter_by(first_name=first_name).all()
    return contact


async def get_contacts_by_last_name(last_name: str, db: Session):
    contact = db.query(Contact).filter_by(last_name=last_name).all()
    return contact


async def get_contact_by_email(email: str, db: Session):
    contact = db.query(Contact).filter_by(email=email).first()
    return contact


async def get_contact_by_birthday(db: Session):
    day_today = datetime.today().date()
    contacts = db.query(Contact).all()
    cont_bd = []
    next_b_day = datetime(1999, 1, 1).date()
    # print(next_b_day)
    for contact in contacts:
        if day_today.month > contact.date_of_birthday.month:
            next_b_day = contact.date_of_birthday.replace(year=day_today.year + 1)
            print(next_b_day)
        elif day_today.month == contact.date_of_birthday.month and day_today.day > contact.date_of_birthday.day:
            next_b_day = contact.date_of_birthday.replace(year=day_today.year + 1)
            print(next_b_day)
        else:
            next_b_day = contact.date_of_birthday.replace(year=day_today.year)
            print(next_b_day)
        if (next_b_day-day_today).days <=7:
            cont_bd.append(contact)
    return cont_bd
    # return contacts

    #     day_today = datetime.today().date()
    #     next_b_day = self._value.date()
    #     if day_today.month > next_b_day.month:
    #         next_b_day = next_b_day.replace(year=day_today.year + 1)
    #     elif day_today.month == next_b_day.month and day_today.day > next_b_day.day:
    #         next_b_day = next_b_day.replace(year=day_today.year + 1)
    #     else:
    #         next_b_day = next_b_day.replace(year=day_today.year)
    #     return (next_b_day-day_today).days

async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.telephone_number = body.telephone_number
        contact.date_of_birthday = body.date_of_birthday
        db.commit()
    return contact


async def remove(contact_id: int, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact

