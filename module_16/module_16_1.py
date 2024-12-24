from fastapi import FastAPI
app = FastAPI()

@app.get("/user/{user_id}")
async def read_user_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user")
async def read_username_age(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}