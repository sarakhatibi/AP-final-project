from fastapi import APIRouter
from .filter_name_product import router as filter_name_product_router
from .delete import router as delete_router
from .filter_id_product import router as filter_id_product_router
from .add_product import router as add_product_router
from .update_product import router as update_product_router
from .filter_sku import router as filter_sku_router
from .inventory_alert import router as inventory_alert_router
from .filter_price_product import router as filter_price_product_router
from .show_by_price import router as show_by_price_router
from .showall_by_name import router as showall_by_name_router

router = APIRouter()

router.include_router(filter_name_product_router, prefix="", tags=["Products - Filter by Name"])
router.include_router(filter_sku_router, prefix="", tags=["Products - Filter by SKU"])
router.include_router(delete_router, prefix="", tags=["Products - Delete"])
router.include_router(filter_id_product_router, prefix="", tags=["Products - Filter by ID"])
router.include_router(add_product_router, prefix="", tags=["Products - Add"])
router.include_router(update_product_router, prefix="", tags=["Products - Update"])
router.include_router(inventory_alert_router, prefix="", tags=["Products - Inventory Alert"])
router.include_router(filter_price_product_router, prefix="", tags=["Products - Filter by Price"])
router.include_router(show_by_price_router, prefix="", tags=["Products - show_by_price"])
router.include_router(showall_by_name_router, prefix="", tags=["Products - showall_by_name"])