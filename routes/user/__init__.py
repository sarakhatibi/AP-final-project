from fastapi import APIRouter
from delete import router as delete
from signeup import router as signeup
from adit import router as adit
from displayallusers import router as displayallusers
from displayauser import router as displayauser

router = APIRouter(prefix="/providers")


router.include_router(delete)
router.include_router(signeup)
router.include_router(adit)
router.include_router(displayallusers)
router.include_router(displayauser)