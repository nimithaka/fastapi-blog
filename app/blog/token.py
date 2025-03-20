from fastapi import Depends
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from blog import schema


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(data: str, credentials_exception):
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        user_id : int = payload.get("user_id")
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(user_id=user_id, email=email)
        return token_data
    except JWTError:
        raise credentials_exception