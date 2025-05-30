from fastapi import APIRouter, Query
from typing import List, Optional
import json
from .database import get_connection

router = APIRouter()

@router.get("/")
def list_products(category: Optional[str] = None, search: Optional[str] = None):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM products"
    params = []

    if category and search:
        query += " WHERE category = ? AND name LIKE ?"
        params = [category, f"%{search}%"]
    elif category:
        query += " WHERE category = ?"
        params = [category]
    elif search:
        query += " WHERE name LIKE ?"
        params = [f"%{search}%"]

    cursor.execute(query, params)
    products = cursor.fetchall()
    conn.close()

    # Rasm va tags JSON sifatida saqlangan, uni Python obyektiga aylantiramiz
    result = []
    for p in products:
        images = json.loads(p["images"]) if p["images"] else []
        tags = p["tags"].split(",") if p["tags"] else []
        result.append({
            "id": p["id"],
            "name": p["name"],
            "category": p["category"],
            "description": p["description"],
            "price": p["price"],
            "images": images,
            "tags": tags
        })
    return result