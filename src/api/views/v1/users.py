from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.infrastructure.database import get_session

router = APIRouter(tags=["Users"], prefix="/v1/users")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(payload: dict, session: Session = Depends(get_session)): ...
