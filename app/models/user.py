from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    # Связь с моделью Task
    tasks = relationship("Task", back_populates="user")

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users():
    pass

@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass

@router.post("/create")
async def create_user():
    pass

@router.put("/update")
async def update_user():
    pass

@router.delete("/delete")
async def delete_user():
    pass