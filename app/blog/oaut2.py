from fastapi import APIRouter, Depends, HTTPException, status
from blog import schemas, models, database, hashing, token
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .import token





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)