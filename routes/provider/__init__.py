from fastapi import APIRouter
from .addprovider import router as addprovider 
from .delete import router as delete
from .display import router as display
from .edit import router as edit

router = APIRouter(prefix="/providers")

router.include_router(addprovider)
router.include_router(delete)
router.include_router(display)
router.include_router(edit)
