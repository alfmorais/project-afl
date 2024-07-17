from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.infrastructure.database import get_session

router = APIRouter(tags=["Contracts"], prefix="/v1/contracts")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_contract(
    payload: dict,
    session: Session = Depends(get_session),
): ...
