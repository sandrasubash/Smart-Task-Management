from fastapi import FastAPI

from app.core.database import engine, Base

from app.db import base
from app.routes.auth import router as auth_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Task Management System"}

@router.get("/")
def get_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    tasks = db.query(Task).offset(skip).limit(limit).all()

    return tasks

raise HTTPException(
    status_code=404,
    detail="Task not found"
)

from fastapi import FastAPI

from app.core.database import engine, Base

from app.db import base

from app.routes import (
    auth,
    users,
    tasks
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

app.include_router(users.router)

app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Task Management System"}

from fastapi import FastAPI

from app.core.database import (
    engine,
    Base
)

from app.routes.auth import (
    router as auth_router
)


app = FastAPI(
    title="Task Management System"
)


Base.metadata.create_all(
    bind=engine
)


app.include_router(auth_router)


@app.get("/")
def root():

    return {
        "message": "Task Management System API Running"
    }