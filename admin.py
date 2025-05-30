from fastapi import APIRouter
from backend.app.products import products_db
from backend.app.orders import orders_db

router = APIRouter()

@router.get("/admin/stats")
def get_statistics():
    total_products = len(products_db)
    total_orders = len(orders_db)
    total_sales = total_orders  # real daromad hisoblash uchun keyinchalik kengaytiriladi
    popular_products = {}  # keyinchalik ko‘p buyurtma qilingan mahsulotlarni sanaydi
    return {
        "total_products": total_products,
        "total_orders": total_orders,
        "total_sales": total_sales,
        "popular_products": popular_products
    }