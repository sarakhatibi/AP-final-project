from fastapi import APIRouter
from .add import router as add_router
from .delete import router as delete_router
from .status import router as status_router
from .display import router as display_router
from .invoice import router as invoice_router

router = APIRouter()
router.include_router(add_router, prefix="", tags=["Orders - Add"])
router.include_router(delete_router, prefix="", tags=["Orders - Delete"])
router.include_router(status_router, prefix="", tags=["Status "])
router.include_router(display_router, prefix="", tags=["display"])
router.include_router(invoice_router, prefix="", tags=["invoice"])