from fastapi import FastAPI
from routes.order import router as order_router
from routes.provider import router as provider_router
from routes.user import router as user_router
from routes.product import router as product_router
from routes.sales_order import router as sales_order_router
from routes.report import router as report_router
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from database.connection import engine

app=FastAPI()


SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return{"message":"Welcome to our shop!"}

app.include_router(order_router, prefix="/orders", tags=["Orders"])
app.include_router(provider_router, prefix="/providers", tags=["providers"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(sales_order_router, prefix="/sales_order", tags=["sales_order"])
app.include_router(report_router.router, prefix="/report", tags=["report"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)