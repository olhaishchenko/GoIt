from typing import List

from fastapi import Depends, HTTPException, status, Path, APIRouter, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import contacts as repository_contacts
from src.schemas import ContactModel, ContactResponse

router = APIRouter(prefix="/contacts", tags=['contacts'])


@router.get("/", response_model=List[ContactResponse], name="All contacts")
async def get_contacts(limit: int = Query(10, le=500), offset: int = 0, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(limit, offset, db)
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='NOT_FOUND')
    return contacts


@router.get("/by_id/{contact_id}", response_model=ContactResponse)
async def get_contact_by_id(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.get("/by_first_name/{first_name}", response_model=List[ContactResponse])
async def get_contacts_by_first_name(first_name: str, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts_by_first_name(first_name, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts


@router.get("/by_last_name/{last_name}", response_model=List[ContactResponse])
async def get_contacts_by_last_name(last_name: str, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts_by_last_name(last_name, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts


@router.get("/by_email/{email}", response_model=List[ContactResponse])
async def get_contact_by_email(email: str, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(email, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.get("/by_birthday/{birthday}", response_model=List[ContactResponse])
async def get_contact_by_birthday(db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_birthday(db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(body.email, db)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is exists')

    contact = await repository_contacts.create(body, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.remove(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(contact)
    db.commit()
    return contact