from src.api.views.v1.companies import router as companies_routers
from src.api.views.v1.contracts import router as contracts_routers
from src.api.views.v1.token import router as token_routers
from src.api.views.v1.users import router as users_routers

__all__ = [
    "companies_routers",
    "contracts_routers",
    "token_routers",
    "users_routers",
]
