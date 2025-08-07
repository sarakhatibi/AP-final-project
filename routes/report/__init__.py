from .provider_report import router as provider_report_router
from fastapi import APIRouter
router = APIRouter()

router.include_router(provider_report_router, prefix="", tags=["report - provider_report"])