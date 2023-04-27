from datetime import datetime, timedelta, date

from sqlalchemy.orm import Session
from sqlalchemy import and_

from src.database.models import Contact, User
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, user: User, db: Session):
    """
    The get_contacts function returns a list of contacts for the user.

    :param skip: int: Skip a number of contacts in the database
    :param limit: int: Limit the number of contacts returned
    :param user: User: Get the user_id of the current user
    :param db: Session: Pass the database session to the function
    :return: A list of contacts
    :doc-author: Trelent
    """
    contacts = db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()
    return contacts


async def get_contact_by_id(contact_id: int, user: User, db: Session):
    """
    The get_contact_by_id function takes in a contact_id and user, and returns the contact with that id.
        Args:
            contact_id (int): The id of the desired Contact object.
            user (User): The User object associated with this Contact.

    :param contact_id: int: Identify the contact to be returned
    :param user: User: Get the user id from the database
    :param db: Session: Pass the database session to the function
    :return: A contact object
    :doc-author: Trelent
    """
    contact = db.query(Contact).filter(and_(id == contact_id, Contact.user_id == user.id)).first()
    return contact


async def get_contacts_body_field(body_field, body_param: str, user: User, db: Session):
    """
    The get_contacts_body_field function is a helper function that returns the contact(s) with the specified body_field
        and body_param. The user parameter is used to ensure that only contacts belonging to the user are returned.

    :param body_field: Specify the field in the contact table that is being queried
    :param body_param: str: Get the value of the body field
    :param user: User: Get the user_id from the user object
    :param db: Session: Access the database
    :return: A list of contacts that match the body_param
    :doc-author: Trelent
    """
    contact = db.query(Contact).filter(
        and_(getattr(Contact, body_field) == body_param, Contact.user_id == user.id)).all()
    return contact


async def get_contact_by_birthday(db: Session):
    """
    The get_contact_by_birthday function returns a list of contacts whose birthday is within the next 7 days.


    :param db: Session: Connect to the database and query it
    :return: A list of contacts whose birthday is in the next 7 days
    :doc-author: Trelent
    """
    day_today = datetime.today().date()
    contacts = db.query(Contact).all()
    cont_bd = []
    for contact in contacts:
        next_b_day = contact.date_of_birthday.replace(year=day_today.year)
        difference = (next_b_day - day_today).days
        print(difference)
        if 0 <= difference <= 7:
            cont_bd.append(contact)
    return cont_bd


async def create(body: ContactModel, db: Session):
    """
    The create function creates a new contact in the database.
        It takes a ContactModel object as input and returns the newly created contact.

    :param body: ContactModel: Get the data from the request body
    :param db: Session: Access the database
    :return: The contact object
    :doc-author: Trelent
    """
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, user: User, body: ContactModel, db: Session):
    """
    The update_contact function updates a contact in the database.
        Args:
            contact_id (int): The id of the contact to update.
            user (User): The user who is updating the contact. This is used to ensure that only contacts belonging to this user are updated.
            body (ContactModel): A ContactModel object containing all the information for this new contact, including first name, last name, email address and telephone number.

    :param contact_id: int: Get the contact by id
    :param user: User: Get the user_id from the user object
    :param body: ContactModel: Pass the new contact information to the function
    :param db: Session: Create a database session
    :return: The updated contact
    :doc-author: Trelent
    """
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.telephone_number = body.telephone_number
        contact.date_of_birthday = body.date_of_birthday
        db.commit()
    return contact


async def remove(contact_id: int, user: User, db: Session):
    """
    The remove function removes a contact from the database.
        Args:
            contact_id (int): The id of the contact to be removed.
            user (User): The user who is removing the contact.
            db (Session): A connection to our database, used for querying and updating data.

    :param contact_id: int: Specify the id of the contact to be removed
    :param user: User: Get the user's id
    :param db: Session: Pass the database session to the function
    :return: The contact that was removed
    :doc-author: Trelent
    """
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
