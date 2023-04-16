from datetime import datetime, timedelta, date

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Contact, User
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, user: User, db: Session):
    contacts = db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()
    return contacts


async def get_contact_by_id(contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter(and_(id == contact_id, Contact.user_id == user.id)).first()
    return contact


async def get_contacts_by_first_name(first_name: str, user: User, db: Session):
    contact = db.query(Contact).filter(and_(first_name==first_name, Contact.user_id == user.id)).all()
    return contact


async def get_contacts_by_last_name(last_name: str, user: User, db: Session):
    contact = db.query(Contact).filter(and_(last_name==last_name, Contact.user_id == user.id)).all()
    return contact


async def get_contact_by_email(email: str, user: User, db: Session):
    contact = db.query(Contact).filter(and_(email==email, Contact.user_id == user.id)).first()
    return contact


async def get_contact_by_birthday(db: Session):
    day_today = datetime.today().date()
    contacts = db.query(Contact).all()
    cont_bd = []
    for contact in contacts:
        next_b_day = contact.date_of_birthday.replace(year=day_today.year)
        difference = (next_b_day-day_today).days
        print(difference)
        if 0 <= difference <= 7:
            cont_bd.append(contact)
    return cont_bd


async def create(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, user: User, body: ContactModel, db: Session):
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.telephone_number = body.telephone_number
        contact.date_of_birthday = body.date_of_birthday
        db.commit()
    return contact


async def remove(contact_id: int, user:User, db: Session):
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact

