from fastapi import APIRouter
from app.orders import orders_db
from collections import Counter

router = APIRouter()

@router.get("/stats")
def get_stats():
    total_orders = len(orders_db)
    item_counter = Counter()

    for order in orders_db:
        for item in order["items"]:
            item_counter[item["name"]] += item["quantity"]

    top_selling = item_counter.most_common(5)

    return {
        "total_orders": total_orders,
        "top_selling": top_selling
    }
