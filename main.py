from fastapi import FastAPI
from routers import product_router, store_router


app = FastAPI()

app.include_router(router=product_router.router, prefix="/products", tags=["products"])
app.include_router(router=store_router.router, prefix="/stores", tags=["stores"])
