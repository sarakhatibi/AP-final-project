from fastapi import APIRouter
from routes.user.login import router as login_router
from .signeup import router as signeup_router
from .edit import router as edit_router
from .displayauser import router as displayauser_router
from .displayallusers import router as displayallusers_router
from .delete import router as delete_router
from .wallet import router as wallet_router  
from .admin_create_user import router as admin_create_user_router

router = APIRouter()

router.include_router(signeup_router, prefix="", tags=["Users - Signeup"])
router.include_router(login_router, prefix="", tags=["Users - login"])
router.include_router(edit_router, prefix="", tags=["Users - Edit"])
router.include_router(displayauser_router, prefix="", tags=["Users - Display Single"])
router.include_router(displayallusers_router, prefix="", tags=["Users - Display All"])
router.include_router(delete_router, prefix="", tags=["Users - Delete"])
router.include_router(wallet_router, prefix="", tags=["Users - wallet"])  
router.include_router(admin_create_user_router, prefix="", tags=["Users - Admin Create"])