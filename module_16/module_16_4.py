from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
users = []  # Список пользователей

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# GET /users
@app.get("/users")
async def get_users():
    return users

# POST /user/{username}/{age}
@app.post("/user/{username}/{age}")
async def create_user(    username: Annotated[str, 
                        Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$",
                             description= "Enter username",
                             examples= "UrbanUser")], 
    age: Annotated[int,
                   Path(ge=18,
                        le=120,
                        description= "Enter age",
                        examples= 24)]
                   ):
    if len(users) == 0:
        new_user = User(id=1, username=username, age=age)
    else:
        new_user = User(
            id=max([user.id for user in users]) + 1, 
            username=username,
            age=age
        )
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int,
                        Path(ge=1,
                        le=100,
                        description= "Enter User ID",
                        examples= 1)],
    username: Annotated[str, 
                        Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$",
                             description= "Enter username",
                             examples= "UrbanUser")], 
    age: Annotated[int,
                   Path(ge=18,
                        le=120,
                        description= "Enter age",
                        examples= 24)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}/")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")

# uvicorn Urban-university.module_16.module_16_4:app