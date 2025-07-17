from fastapi import APIRouter
from .login import router as login_router
from .signeup import router as signeup_router
from .edit import router as edit_router
from .displayauser import router as displayauser_router
from .displayallusers import router as displayallusers_router
from .delete import router as delete_router

router = APIRouter(prefix="/users")

router.include_router(signeup_router, prefix="/signup", tags=["Users - Signeup"])
router.include_router(login_router, prefix="/login", tags=["Users - login"])
router.include_router(edit_router, prefix="/edit", tags=["Users - Edit"])
router.include_router(displayauser_router, prefix="/display", tags=["Users - Display Single"])
router.include_router(displayallusers_router, prefix="/displayall", tags=["Users - Display All"])
router.include_router(delete_router, prefix="/delete", tags=["Users - Delete"])
