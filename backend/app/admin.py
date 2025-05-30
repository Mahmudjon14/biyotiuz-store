from fastapi import APIRouter, HTTPException
from collections import Counter
from app.orders import orders_db

router = APIRouter()

@router.get("/orders")
def get_all_orders():
    return {"orders": orders_db}

@router.put("/orders/{order_id}/status")
def update_order_status(order_id: str, status: str):
    for order in orders_db:
        if order["id"] == order_id:
            order["status"] = status
            return {"message": f"Buyurtma holati '{status}' ga yangilandi"}
    raise HTTPException(status_code=404, detail="Buyurtma topilmadi")

@router.get("/stats")
def get_stats():
    total_orders = len(orders_db)
    item_counter = Counter()

    for order in orders_db:
        for item in order.get("items", []):
            item_counter[item["name"]] += item["quantity"]

    top_selling = item_counter.most_common(5)

    return {
        "total_orders": total_orders,
        "top_selling": top_selling
    }
