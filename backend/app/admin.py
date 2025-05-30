from fastapi import APIRouter
from backend.app.database import admin_db  # To‘g‘rilangan import

router = APIRouter()

@router.get("/")
async def get_admin_info():
    return admin_db
