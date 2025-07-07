from fastapi import FastAPI
from routes.order import router as order_router

app=FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to our shop!"}

app.include_router(order_router, tags=["Orders"])