from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import products, orders, admin  # Keyingi fayllardan import qilamiz

app = FastAPI()

# Frontend bilan bog‘lanish uchun CORS sozlamalari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ishlab chiqarishda domenni aniqlang
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routerni ulash
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Biyoti Uz mini app backend ishga tushdi!"}
