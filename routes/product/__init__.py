from fastapi import APIRouter
from .filter_name_product import router as filter_name_product 
from .delete import router as delete
from .filter_id_product import router as filter_id_product
from .add_product import router as add_product
from .update_product import router as update_product
from .filter_sku import router as filter_sku
from .inventory_alert import router as inventory_alert 
router = APIRouter(prefix="/products")

router.include_router(filter_name_product)
router.include_router(filter_sku)
router.include_router(delete)
router.include_router(filter_id_product)
router.include_router(add_product)
router.include_router(update_product)
router.include_router(inventory_alert )