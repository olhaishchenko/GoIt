from typing import List

from fastapi import FastAPI, Depends, HTTPException, status, Path, APIRouter, Query
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import Cat
from src.schemas import CatModel, CatResponse, CatVaccinatedModel

router = APIRouter(prefix="/cats", tags=['cats'])


@router.get("/cats", response_model=List[CatResponse])
async def get_cats(limit: int = Query(10, le=500), offset: int = 0, db: Session = Depends(get_db)):
    cats = db.query(Cat).limit(limit).offset(offset).all()
    return cats


@router.get("/{cat_id}", response_model=CatResponse)
async def get_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return cat


@router.post("/", response_model=CatResponse, status_code=status.HTTP_201_CREATED)
async def create_cat(body: CatModel, db: Session = Depends(get_db)):
    cat = Cat(**body.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@router.put("/{cat_id}", response_model=CatResponse)
async def update_cat(body: CatModel, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    cat.nickname = body.nickname
    cat.age = body.age
    cat.vaccinated = body.vaccinated
    cat.description = body.description
    cat.owner_id = body.owner_id
    db.commit()
    return cat


@router.delete("/{cat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_cat(cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    db.delete(cat)
    db.commit()
    return cat


@router.patch("/{cat_id}/vaccinated", response_model=CatResponse)
async def vaccinated_cat(body: CatVaccinatedModel, cat_id: int = Path(ge=1), db: Session = Depends(get_db)):
    cat = db.query(Cat).filter_by(id=cat_id).first()
    if cat is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    cat.vaccinated = body.vaccinated
    db.commit()
    return cat