from fastapi import APIRouter
from .get_all_order import router as get_all_router
from .get_order_by_id import router as get_by_id_router
from .add_order import router as add_router
from .update_order import router as update_router
from .delete import router as delete_router

router = APIRouter(prefix="/orders")

router.include_router(get_all_router, prefix="", tags=["Orders - Get All"])
router.include_router(get_by_id_router, prefix="", tags=["Orders - Get By ID"])
router.include_router(add_router, prefix="", tags=["Orders - Add"])
router.include_router(update_router, prefix="", tags=["Orders - Update"])
router.include_router(delete_router, prefix="", tags=["Orders - Delete"])
