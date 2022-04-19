from typing import Optional, List
from pydantic import BaseModel
from models.product_models import ProductPydantic


class StorePydantic(BaseModel):
    id: int
    name: str
    location: str


class StorePydanticCreate(BaseModel):
    name: str
    location: str


class StorePydanticPatch(BaseModel):
    name: Optional[str]
    location: Optional[str]


class StoreProductsPydantic(BaseModel):
    store: StorePydantic
    products: Optional[List[ProductPydantic]]


