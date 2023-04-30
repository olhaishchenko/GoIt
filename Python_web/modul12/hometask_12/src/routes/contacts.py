from typing import List

from fastapi import Depends, HTTPException, status, Path, APIRouter, Query
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter

from src.conf.detail import NOT_FOUND, EMAIL_IS_EXISTS
from src.database.db import get_db
from src.database.models import User, Role
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel, ContactResponse
from src.services.auth import auth_service
from src.services.roles import RoleAccess

router = APIRouter(prefix="/contacts", tags=['contacts'])

allowed_operation_get = RoleAccess([Role.admin, Role.moderator, Role.user])
allowed_operation_create = RoleAccess([Role.admin, Role.moderator, Role.user])
allowed_operation_update = RoleAccess([Role.admin, Role.moderator])
allowed_operation_remove = RoleAccess([Role.admin])


@router.get("/", response_model=List[ContactResponse], name="All contacts",
            dependencies=[Depends(allowed_operation_get), Depends(RateLimiter(times=2, seconds=5))])
async def get_contacts(skip: int = 0, limit: int = 100, offset: int = 10, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    """
    The **get_contacts** function returns a list of contacts.
        The function takes in the following parameters:
            skip (int): The number of items to skip before starting to collect the result set. Default is 0.
            limit (int): The numbers of items to return after skipping 'skip' items. Default is 100, max is 1000.
            offset (int): Used for pagination, this will determine how many pages are returned based on limit and offset values.

    :param skip: int: Skip the first n contacts in the database
    :param limit: int: Limit the number of contacts returned
    :param offset: int: Skip the first 10 contacts
    :param db: Session: Get a database session
    :param current_user: User: Get the current user from the database
    :return: A list of contacts
    :doc-author: Trelent
    """
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(allowed_operation_get)])
async def get_contact_by_id(contact_id: int, db: Session = Depends(get_db),
                            current_user: User = Depends(auth_service.get_current_user)):
    """
    The **get_contact_by_id** function is used to retrieve a contact by its id.
        The function takes in the following parameters:
            - contact_id: int, the id of the contact to be retrieved.
            - db: Session = Depends(get_db), an instance of a database session that will be used for querying data from
                and persisting data into our database. This parameter is optional as it has been assigned a default value
                using dependency injection (i.e., Depends(get_db)). Dependency injection allows us to inject dependencies
                into functions without having to instantiate them

    :param contact_id: int: Get the contact_id from the url
    :param db: Session: Pass the database session to the function
    :param current_user: User: Get the current user
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.get_contact_by_id(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    return contact


@router.get("/{body_field}/{body_param}", response_model=List[ContactResponse],
            dependencies=[Depends(allowed_operation_get)])
async def get_contacts_body_field(body_field, body_param: str, db: Session = Depends(get_db),
                                     current_user: User = Depends(auth_service.get_current_user)):
    """
    The **get_contacts_body_field** function is used to get a list of contacts from the database.
    The function takes in a body_field parameter, which is the field that you want to search for in the database.
    It also takes in a body_param parameter, which is what you are searching for within that field.
    The function returns an array of contacts.

    :param body_field: Specify which field in the body of the contact you want to search for
    :param body_param: str: Specify the body field that is being searched for
    :param db: Session: Access the database
    :param current_user: User: Get the user id of the current logged-in user
    :return: A list of contacts that have the same value for a specified body field
    :doc-author: Trelent
    """
    contacts = await repository_contacts.get_contacts_body_field(body_field, body_param, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    return contacts


@router.get("/by_birthday/{birthday}", response_model=List[ContactResponse],
            dependencies=[Depends(allowed_operation_get)])
async def get_contact_by_birthday(db: Session = Depends(get_db),
                                  current_user: User = Depends(auth_service.get_current_user)):
    """
    The **get_contact_by_birthday** function returns the contact with the closest birthday to today.
        If no contacts are found, a 404 error is returned.

    :param db: Session: Pass the database session to the function
    :param current_user: User: Get the current user from the database
    :return: A contact object
    :doc-author: Trelent
    """
    contact = await repository_contacts.get_contact_by_birthday(db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(allowed_operation_create), Depends(RateLimiter(times=2, seconds=120))])
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    """
    The **create_contact** function creates a new contact in the database.

    :param body: ContactModel: Define the data that is required to create a contact
    :param db: Session: Get the database session
    :param current_user: User: Get the current user from the database
    :return: A ContactModel object
    :doc-author: Trelent
    """
    contact = await repository_contacts.get_contacts_body_field('email', body.email, current_user, db)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=EMAIL_IS_EXISTS)

    contact = await repository_contacts.create(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse, dependencies=[Depends(allowed_operation_update)])
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    """
    The **update_contact** function updates a contact in the database.
        The function takes an id, body and db as parameters.
        It returns a ContactModel object.

    :param body: ContactModel: Get the data from the request body
    :param contact_id: int: Get the contact_id from the url
    :param db: Session: Access the database
    :param current_user: User: Get the current user from the database
    :return: A ContactModel object
    :doc-author: Trelent
    """
    contact = await repository_contacts.update_contact(contact_id, current_user, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(allowed_operation_remove)])
async def remove_contact(contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    """
    The **remove_contact** function removes a contact from the database.
        The function takes in an integer representing the id of the contact to be removed,
        and returns a dictionary containing information about that contact.

    :param contact_id: int: Identify the contact to be removed
    :param db: Session: Pass the database session to the repository layer
    :param current_user: User: Get the current user
    :return: The contact that was removed
    :doc-author: Trelent
    """
    contact = await repository_contacts.remove(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
    db.delete(contact)
    db.commit()
    return contact
