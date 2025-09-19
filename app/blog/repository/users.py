from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from blog.repository import  users
from blog.hashing import Hash




get_db = database.get_db




def create(request:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def show(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with the id {id} is not available")
    return user