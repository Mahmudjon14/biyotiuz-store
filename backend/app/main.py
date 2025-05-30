from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Biyoti Uz mini app API ishlamoqda!"}
