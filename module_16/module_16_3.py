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
def register_user(username, age):
    user_id = int(max(users.keys())) + 1
    users[user_id] = f'Имя: {username}, возраст: {age}' 
    return f'User {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found") 
    del users[user_id]
    return {"message": f"User {user_id} has been deleted"}


# uvicorn Urban-university.module_16.module_16_2:app