from fastapi import APIRouter, Request
from datetime import datetime
import uuid

router = APIRouter()

orders_db = []

@router.post("/")
async def create_order(request: Request):
    data = await request.json()
    order_id = str(uuid.uuid4())
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    order = {
        "id": order_id,
        "name": data.get("name"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "items": data.get("items"),
        "time": order_time,
        "status": "Yangi"
    }
    orders_db.append(order)
    return {"message": "Buyurtma qabul qilindi", "order_id": order_id}

@router.get("/")
def get_orders():
    return {"orders": orders_db}
