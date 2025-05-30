from fastapi import APIRouter
from backend.app.database import orders_db  # To‘g‘rilangan import

router = APIRouter()

@router.get("/")
async def get_all_orders():
    return orders_db
