from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
templates = Jinja2Templates(directory= 'Urban-university/module_16/templates')
app = FastAPI()
users = [] 


class User(BaseModel):
    id: int
    username: str
    age: int

#выводим весь список пользователей
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, 'users': users})

#получаем доступ к пользователю по id либо выводим что пользователь не найден
@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int):
    try:
        user = next((user for user in users if user.id == user_id))
        return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')

@app.delete("/user/{user_id}/")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
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
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# uvicorn Urban-university.module_16.module_16_5:app