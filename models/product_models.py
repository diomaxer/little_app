from typing import Optional

from pydantic import BaseModel


class ProductPydantic(BaseModel):
    id: int
    store_id: int
    name: str
    price: int


class ProductPydanticCreate(BaseModel):
    store_id: int
    name: str
    price: int


class ProductPydanticPatch(BaseModel):
    store_id: Optional[int]
    name: Optional[str]
    price: Optional[int]
