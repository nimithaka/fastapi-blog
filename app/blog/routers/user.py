from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from blog import schema, database, models
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)

get_db = database.get_db
@router.post('/', response_model=schema.showUser)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schema.showUser)
def show_user(id: int,db: Session = Depends(get_db)):
    return user.get(id, db)