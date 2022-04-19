from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.models.store_models import StorePydantic, StoreProductsPydantic, StorePydanticPatch, StorePydanticCreate
from src.database.dependencies import get_db
from src.services.store_service import StoreService

router = APIRouter()


@router.get(
    path="/",
    description="Get all stores",
    status_code=status.HTTP_200_OK,
    tags=['stores'],
    response_model=List[StorePydantic],
)
async def get_products(db_session: Session = Depends(get_db)):
    return await StoreService.get_all_stores(db_session=db_session)


@router.get(
    path="/{store_id}",
    description="Get store by id",
    status_code=status.HTTP_200_OK,
    tags=['stores'],
    response_model=StoreProductsPydantic,
)
async def get_store_by_id(store_id: int, db_session: Session = Depends(get_db)):
    return await StoreService.get_store_by_id(store_id=store_id, db_session=db_session)


@router.patch(
    path="/update/{store_id}",
    description="Update store",
    status_code=status.HTTP_200_OK,
    tags=['stores'],
    # response_model=ProductPydantic,
)
async def update_product(store_id: int, store: StorePydanticPatch, db_session: Session = Depends(get_db)):
    return await StoreService.update_store(store_id=store_id, store=store, db_session=db_session)


@router.post(
    path="/add_store/",
    description="Create store",
    status_code=status.HTTP_200_OK,
    tags=['stores'],
    response_model=StorePydantic,
)
async def add_product(store: StorePydanticCreate, db_session: Session = Depends(get_db)):
    return await StoreService.add_store(store=store, db_session=db_session)


@router.delete(
    path="/delete/{store_id}",
    description="Delete product by id",
    status_code=status.HTTP_200_OK,
    tags=['stores'],
)
async def delete_product(store_id: int, db_session: Session = Depends(get_db)):
    return await StoreService.delete_store_by_id(store_id=store_id, db_session=db_session)
