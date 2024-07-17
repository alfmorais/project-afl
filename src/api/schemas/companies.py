from typing import Annotated, List

from fastapi import File, UploadFile
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator,
)
from validate_docbr.CNPJ import CNPJ


class CompanyInput(BaseModel):
    nickname: str = Field(max_length=128, description="Apelido da Empresa")
    trade_name: str = Field(max_length=128, description="Nome Fantasia")
    legal_name: str = Field(max_length=256, description="Razao Social")
    document: str = Field(pattern=r"^\d{14}$", description="CNPJ")
    state: str = Field(pattern=r"^[A-Z]{2}$", description="Sigla do Estado")
    city: str = Field(max_length=128, description="Cidade")
    # logo_url: UploadFile

    @field_validator("document")
    @classmethod
    def validate_document(cls, document: str) -> str:
        document_validate = CNPJ()

        if document_validate.validate(document):
            return document

        raise ValidationError()

    class Config:
        str_min_length = 1
        str_strip_whitespace = True


class CompanyOutput(CompanyInput):
    id: int


class CompaniesOutput(BaseModel):
    companies: List[CompanyOutput]


class CompanyMessage(BaseModel):
    message: str
