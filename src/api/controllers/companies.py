from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import CompanyInput
from src.api.models import Company


class CompaniesController:
    def __init__(self, model = Company) -> None:
        self.model = model

    def create(self, payload: CompanyInput, session: Session): ...
    def read(self, session: Session): ...
    def delete(self, id: int, session: Session):
        statement = select(self.model).where((self.model.id == id))
        company = session.scalar(statement)

        if company:
            session.delete(company)
            session.commit()
            return {
                "message": f"Empresa com o ID {id} deletado do banco de dados"
            }

        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f"Empresa com o ID {id} não encontrado",
        )


companies_controller = CompaniesController()
