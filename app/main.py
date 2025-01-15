

# uvicorn UrbanUniversity.app.main:app
from fastapi import FastAPI
# from routers.task import router as task_router
# from routers.user import router as user_router
from routers import task
from routers import user
from app.routers import task
from app.routers import user



app = FastAPI()

@app.get("/")
def welcome_message():
    return {"message": "Welcome to Taskmanager"}

# app.include_router(task_router, prefix="/task", tags=["task"])
# app.include_router(user_router, prefix="/user", tags=["user"])
# app.include_router(category.router)
app.include_router(task.router)
app.include_router(user.router)

