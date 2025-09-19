from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from blog.hashing import Hash 
from blog.repository import users 


get_db = database.get_db


router = APIRouter(
    prefix="/user",
    tags=['Users']
)






@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session = Depends(get_db)):
 
   return users.create(request, db)



@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db:Session = Depends(get_db)):
    return users.show(id, db)