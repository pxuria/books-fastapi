from fastapi import APIRouter
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Path
from models import Todos, Users
from database import SessionLocal
from starlette import status
from .auth import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all_todos(user: user_dependency, db: db_dependency):
    if user is None or user.get("role") != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed."
        )
    return db.query(Todos).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)
):
    if user is None or user.get("role") == "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed."
        )

    todo_model = db.query(Todos).filter(Todos.id == todo_id)

    if todo_model.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="todo not found"
        )

    todo_model.delete()
    db.commit()


@router.get("/users", status_code=status.HTTP_200_OK)
async def read_all_users(user: user_dependency, db: db_dependency):
    if user is None or user.get("role") != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed."
        )
    return db.query(Users).all()
