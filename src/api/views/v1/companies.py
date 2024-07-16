from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.infrastructure.database import get_session

router = APIRouter(tags=["Companies"], prefix="/v1/companies")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_company(payload: dict, session: Session = Depends(get_session)): ...


@router.get("", status_code=status.HTTP_200_OK)
def read_company(session: Session = Depends(get_session)): ...


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(id: int, session: Session = Depends(get_session)): ...
