from .provider_report import router as provider_report_router
from .sales_report import router as sales_report_router
from fastapi import APIRouter
router = APIRouter()

router.include_router(provider_report_router, prefix="", tags=["report - provider_report"])
router.include_router(sales_report_router, prefix="", tags=["report - sales_report"])
