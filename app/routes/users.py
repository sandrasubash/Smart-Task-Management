from fastapi import APIRouter, Depends, HTTPException

from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/admin")
def admin_route(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return {"message": "Welcome Admin"}