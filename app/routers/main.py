

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
app.include_router(task.models)
app.include_router(user.models)

