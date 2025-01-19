

# uvicorn Urban-university.app.main:app
# uvicorn app.main:app
from fastapi import FastAPI
# from routers.task import router as task_router
# from routers.user import router as user_router

from routers import user
from routers import task
# from app.routers import 



app = FastAPI()

@app.get("/")
def welcome_message():
    return {"message": "Welcome to Taskmanager"}

# app.include_router(category.router)
app.include_router(task.router)
app.include_router(user.router)

