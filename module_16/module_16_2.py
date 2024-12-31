from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from typing import Dict
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root() -> str:
    return ("Главная страница")

@app.get("/user/{user_id}")
async def read_user_id(
    user_id: Annotated[int,
                        Path(ge=1,
                        le=100,
                        description= "Enter User ID",
                        examples= 1)]
    ):
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user/{username}/{age}")
async def read_username_age(
    username: Annotated[str, 
                        Path(ge=5,
                             le=20,
                             description= "Enter username",
                             examples= "UrbanUser")], 
    age: Annotated[int,
                   Path(ge=18,
                        le=120,
                        description= "Enter age",
                        examples= 24)]
    ):
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")

@app.get("/user/admin")
async def read_admin() -> str:
    return ("Вы вошли как администратор")


# uvicorn Urban-university.module_16.module_16_1:app