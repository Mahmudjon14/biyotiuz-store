from fastapi import FastAPI
from backend.app.products import router as products_router
from backend.app.orders import router as orders_router
from backend.app.admin import router as admin_router

app = FastAPI()

app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Biyoti Uz mini app API ishlamoqda!"}
