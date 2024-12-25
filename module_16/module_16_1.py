from fastapi import *
app = FastAPI()

@app.get("/user/admin")
async def read_admin() -> str:
    return ("Вы вошли как администратор")

@app.get("/user/{user_id}")
async def read_user_id(user_id: int) -> str:
    return (f"Вы вошли как пользователь № {user_id}")

@app.get("/user")
async def read_username_age(username: str, age: int) -> str:
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")

@app.get("/")
async def read_root() -> str:
    return ("Главная страница")
# uvicorn Urban-university.module_16.module_16_1:app

# if __name__ == '__main__':
#     app.run()
    
# cd Urban_university/main.py    
# >> python -m uvicorn main:app
# uvicorn main:app --reload
# Urban-university.module_16.main:app --reload