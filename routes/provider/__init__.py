from fastapi import APIRouter
from .addprovider import router as addprovider_router
from .delete import router as delete_router
from .display import router as display_router
from .edit import router as edit_router

router = APIRouter(prefix="/providers")

router.include_router(addprovider_router, prefix="/add", tags=["Providers - Add"])
router.include_router(delete_router, prefix="/delete", tags=["Providers - Delete"])
router.include_router(display_router, prefix="/display", tags=["Providers - Display"])
router.include_router(edit_router, prefix="/edit", tags=["Providers - Edit"])
