from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from blog import schema, database, oauth2
from blog.repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=List[schema.showBlog])
def all(db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request : schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    # return {'title': request.title, 'body': request.body}
    return blog.create(request, db, current_user)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def deleteBlog(id: int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id: int, request : schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schema.showBlog)
def show(id: int, db: Session = Depends(database.get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
   return blog.show(id, db)