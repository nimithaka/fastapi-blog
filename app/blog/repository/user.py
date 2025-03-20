from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schema
from blog.hashing import Hash


def create(request: schema.User, db: Session):
    new_user = models.User(name = request.name, email = request.email, password = Hash.brypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'user with the id {id} is not found')
    return user
