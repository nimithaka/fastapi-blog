from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import schema, database, models
from blog.hashing import Hash
from blog.token import create_access_token


router = APIRouter(
    tags=['Login']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'invalid username')
    if not Hash.verify(request.password, user.password):
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'password is incorrect')
    
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email, "user_id": user.id}
    )
    return {"access_token" :access_token, "token_type": "bearer"}

    
