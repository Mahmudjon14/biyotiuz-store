from fastapi import APIRouter
from backend.app.database import products_db  # To‘g‘rilangan import

router = APIRouter()

@router.get("/")
async def get_all_products():
    return products_db
