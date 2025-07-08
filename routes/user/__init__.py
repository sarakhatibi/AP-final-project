from fastapi import APIRouter
from .signeup import router as signeup
from .edit import router as edit
from .displayauser import router as displayauser
from .displayallusers import router as displayallusers
from .delete import router as delete

router = APIRouter(prefix="/users")

router.include_router(signeup)
router.include_router(edit)
router.include_router(displayauser)
router.include_router(displayallusers)
router.include_router(delete)