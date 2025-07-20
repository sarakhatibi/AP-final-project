from fastapi import APIRouter
from .add import router as add_router
from .status import router as status_router
from .display import router as display_router


router = APIRouter()
router.include_router(add_router, prefix="", tags=["Orders - Add"])
router.include_router(status_router, prefix="", tags=["Status "])
router.include_router(display_router, prefix="", tags=["display"])
