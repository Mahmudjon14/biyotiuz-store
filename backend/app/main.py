from fastapi import FastAPI
from products import router as products_router
from orders import router as orders_router
from admin import router as admin_router

app = FastAPI()

app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Biyoti Uz mini app API ishlamoqda!"}
