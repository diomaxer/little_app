import sys
sys.path.append("..")

from fastapi import FastAPI
from src.routers import product_router, shops_router


app = FastAPI()

app.include_router(router=product_router.router, prefix="/products", tags=["products"])
app.include_router(router=shops_router.router, prefix="/shops", tags=["shops"])
