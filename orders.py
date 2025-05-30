from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from datetime import datetime

router = APIRouter()

# Buyurtma modeli
class Order(BaseModel):
    id: str
    user_name: str
    phone_number: str
    address: str
    products: List[str]
    status: str = "Yangi"
    created_at: str

# Xotirada saqlanadigan buyurtmalar ro'yxati (hozircha database yo'q)
orders_db = []

# Buyurtma qo‘shish
@router.post("/orders/")
def create_order(order_data: Order):
    order_data.id = str(uuid4())
    order_data.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    orders_db.append(order_data)
    return {"message": "Buyurtma qabul qilindi", "order_id": order_data.id}

# Barcha buyurtmalarni olish (admin uchun)
@router.get("/orders/")
def get_orders():
    return orders_db

# Buyurtma statusini o‘zgartirish
@router.put("/orders/{order_id}/status")
def update_order_status(order_id: str, status: str):
    for order in orders_db:
        if order.id == order_id:
            order.status = status
            return {"message": "Status yangilandi"}
    raise HTTPException(status_code=404, detail="Buyurtma topilmadi")