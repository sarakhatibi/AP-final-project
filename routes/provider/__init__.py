from fastapi import APIRouter
from .addprovider import router as addprovider_router
from .delete import router as delete_router
from .display import router as display_router
from .edit import router as edit_router
from .showbyid import router as showbyid_router

router = APIRouter()

router.include_router(addprovider_router, prefix="", tags=["Providers - Add"])
router.include_router(delete_router, prefix="", tags=["Providers - Delete"])
router.include_router(display_router, prefix="", tags=["Providers - Display"])
router.include_router(edit_router, prefix="", tags=["Providers - Edit"])
router.include_router(showbyid_router, prefix="", tags=["showbyid - Add"])
