from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app import products, orders, admin

app = FastAPI(
    title="Biyoti Uz Mini App Backend",
    version="1.0"
)

# Frontend va Telegram uchun CORS ruxsat
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # kerak bo‘lsa, bu yerga frontend URL’larini yozasiz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routerlarni ulash
app.include_router(products.router, prefix="/api")
app.include_router(orders.router, prefix="/api")
app.include_router(admin.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Biyoti Uz backend ishlayapti!"}