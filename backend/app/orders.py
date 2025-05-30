from fastapi import APIRouter, Request
from app.database import orders, generate_id

router = APIRouter()

@router.post("/")
async def create_order(order_data: dict, request: Request):
    order_id = generate_id()
    order_data["id"] = order_id
    order_data["ip"] = request.client.host
    order_data["status"] = "New"
    orders.append(order_data)
    return {"message": "Buyurtma qabul qilindi", "order_id": order_id}

@router.get("/")
async def get_orders():
    return orders
