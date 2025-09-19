from fastapi import APIRouter, Depends, HTTPException, status
from blog import models, database, hashing
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from blog.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

get_db = database.get_db

router = APIRouter(
    tags=["Authentication"]
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # check user exists
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    # verify password (make sure your Hash.verify has correct arg order: plain, hashed)
    if not hashing.Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    # create JWT token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
