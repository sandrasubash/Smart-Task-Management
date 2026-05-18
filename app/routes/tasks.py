from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.models.task import Task

from app.models.user import User

from app.schemas.task import TaskCreate

from app.utils.dependencies import (
    get_db,
    get_current_user
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] not in ["admin", "manager"]:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    user = db.query(User).filter(
        User.id == task.assigned_to
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    new_task = Task(
        title=task.title,
        description=task.description,
        assigned_to=task.assigned_to
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task