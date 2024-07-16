from fastapi import FastAPI

from src.api.views.v1 import (
    companies_routers,
    contracts_routers,
    token_routers,
    users_routers,
)
from src.infrastructure.server.settings import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_TITLE,
            version=settings.PROJECT_VERSION,
        )
        self._include_routers()

    def _include_routers(self) -> None:
        self.include_router(companies_routers)
        self.include_router(contracts_routers)
        self.include_router(token_routers)
        self.include_router(users_routers)


app = App()
