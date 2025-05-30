from fastapi import APIRouter
from app.database import products_db

router = APIRouter()

@router.get("/")
def get_all_products():
    return {"products": products_db}

@router.get("/search")
def search_products(q: str):
    results = [p for p in products_db if q.lower() in p["name"].lower()]
    return {"results": results}
