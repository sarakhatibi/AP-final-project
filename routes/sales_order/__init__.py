from fastapi import APIRouter
from .add import router as add_router


router = APIRouter()
router.include_router(add_router, prefix="", tags=["Orders - Add"])
