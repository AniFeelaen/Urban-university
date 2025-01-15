from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from typing import Dict
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def register_user(
    username: Annotated[str, 
                        Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$",
                             description= "Enter username",
                             examples= "UrbanUser")], 
    age: Annotated[int,
                   Path(ge=18,
                        le=120,
                        description= "Enter age",
                        examples= 24)]
                  ):
    user_id = int(max(users.keys())) + 1
    users[user_id] = f'Имя: {username}, возраст: {age}' 
    return f'User {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int,
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
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found") 
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}


# uvicorn Urban-university.app.module_16_4:app