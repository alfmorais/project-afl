from typing import Annotated
from fastapi import APIRouter, Depends, File, status, UploadFile
from sqlalchemy.orm import Session

from src.api.controllers import companies_controller
from src.api.schemas import (
    CompaniesOutput,
    CompanyInput,
    CompanyMessage,
    CompanyOutput,
)
from src.infrastructure.database import get_session

router = APIRouter(tags=["Companies"], prefix="/v1/companies")


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CompanyOutput,
)
def create_company(
    payload: CompanyInput,
    session: Session = Depends(get_session),
):
    return companies_controller.create(payload, session)


@router.post(
    "/{id}/logo",
    status_code=status.HTTP_201_CREATED,
    # response_model=CompanyOutput,
)
def create_company_logo(
    id: int,
    file: Annotated[bytes, File()],
    session: Session = Depends(get_session),
):
    return {"file": file, "filename": file, "id": id}
    # return companies_controller.create(payload, session)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=CompaniesOutput,
)
def read_company(session: Session = Depends(get_session)):
    return companies_controller.read(session)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CompanyMessage,
)
def delete_company(id: int, session: Session = Depends(get_session)):
    return companies_controller.delete(id, session)
