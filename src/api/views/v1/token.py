from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.infrastructure.database import get_session

router = APIRouter(tags=["Token"], prefix="/v1/token")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_token(
    payload: dict,
    session: Session = Depends(get_session),
): ...


@router.post("/refresh", status_code=status.HTTP_200_OK)
def create_refresh_token(
    payload: dict,
    session: Session = Depends(get_session),
): ...
