from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schema


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request : schema.Blog, db: Session,  current_user: schema.User):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = current_user.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schema.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available to edit')
    blog.update(request.model_dump())
    db.commit() 
    return "updated"

def show(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog