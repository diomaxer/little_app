from typing import List, Optional
from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from src.database.dependencies import get_db
from src.services.product_service import ProductService
from src.models.product_models import ProductPydantic, ProductPydanticCreate, ProductPydanticPatch

router = APIRouter()


@router.get(
    path="/",
    description="Get all products",
    status_code=status.HTTP_200_OK,
    tags=['products'],
    response_model=List[ProductPydantic],
)
async def get_products(db_session: Session = Depends(get_db)):
    return await ProductService.get_all_products(db_session=db_session)


@router.get(
    path="/{product_id}",
    description="Get product by id",
    status_code=status.HTTP_200_OK,
    tags=['products'],
    response_model=ProductPydantic,
)
async def get_product_by_id(product_id: int, db_session: Session = Depends(get_db)):
    return await ProductService.get_product_by_id(product_id=product_id, db_session=db_session)


@router.patch(
    path="/update/{product_id}",
    description="Update product",
    status_code=status.HTTP_200_OK,
    tags=['products'],
    # response_model=ProductPydantic,
)
async def update_product(product_id: int, product: ProductPydanticPatch, db_session: Session = Depends(get_db)):
    return await ProductService.update_product(product_id=product_id, product=product, db_session=db_session)


@router.post(
    path="/add_product/",
    description="Create product",
    status_code=status.HTTP_200_OK,
    tags=['products'],
    response_model=ProductPydantic,
)
async def add_product(product: ProductPydanticCreate, db_session: Session = Depends(get_db)):
    return await ProductService.add_product(product=product, db_session=db_session)


@router.delete(
    path="/delete/{product_id}",
    description="Delete product by id",
    status_code=status.HTTP_200_OK,
    tags=['products'],
)
async def delete_product(product_id: int, db_session: Session = Depends(get_db)):
    return await ProductService.delete_product_by_id(product_id=product_id, db_session=db_session)
