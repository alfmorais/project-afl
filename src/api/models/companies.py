from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database import Base


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    nickname: Mapped[str] = mapped_column(String(128), nullable=False)
    trade_name: Mapped[str] = mapped_column(String(128), nullable=False)
    legal_name: Mapped[str] = mapped_column(String(256), nullable=False)
    document: Mapped[str] = mapped_column(
        String(14), unique=True, nullable=False
    )  # noqa E501
    state: Mapped[str] = mapped_column(String(2), nullable=False)
    city: Mapped[str] = mapped_column(String(128), nullable=False)
    # logo_url: Mapped[Optional[FileUrl] = None

    def __repr__(self) -> str:
        return f"Company[id={self.id}, nickname={self.nickname}]"
