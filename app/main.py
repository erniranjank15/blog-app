from fastapi import FastAPI, Depends, status, responses, Response, HTTPException
from blog import schemas, models,hashing
from blog.database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from blog.hashing import Hash
from blog.routers import blog, user, authentication




app = FastAPI()
    


@app.get("/", status_code=status.HTTP_200_OK, tags=["Root"])
def read_root():
    return {"message": "Welcome to Blog API"}



models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




