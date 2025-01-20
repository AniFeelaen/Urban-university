

# uvicorn Urban-university.app.main:app
# uvicorn app.main:app
from fastapi import FastAPI
from models import user
from models import task


app = FastAPI()

@app.get("/")
def welcome_message():
    return {"message": "Welcome to Taskmanager"}

# app.include_router(category.router)
app.include_router(task.router)
app.include_router(user.router)

from sqlalchemy.schema import CreateTable
print(CreateTable(user.User.__table__))
print(CreateTable(task.Task.__table__))

# alembic revision --autogenerate -m "initial migration2"
# from app.backend.db import Base
# from app.models.user import User
# from app.models.task import Task
# target_metadata = Base.metadata
# sqlite:///taskmanager.db