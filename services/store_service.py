from sqlalchemy.orm import Session

from database.alchemy_models import Store
from managers.product_manager import ProductManager
from models.product_models import ProductPydantic
from managers.store_manager import StoreManager
from models.store_models import StorePydantic, StoreProductsPydantic, StorePydanticPatch, StorePydanticCreate


class StoreService:
    @staticmethod
    async def get_all_stores(db_session: Session):
        stores = await StoreManager.get_all_stores(db_session=db_session)
        if not stores:
            return None
        return [StorePydantic(**store.__dict__) for store in stores]

    @staticmethod
    async def get_store_by_id(store_id: int, db_session: Session):
        store = await StoreManager.get_store_by_id(store_id=store_id, db_session=db_session)
        if not store:
            return None
        products = await ProductManager.get_all_store_products(store_id=store_id, db_session=db_session)
        products = [ProductPydantic(**product.__dict__) for product in products] if products else None

        return StoreProductsPydantic(store=StorePydantic(**store.__dict__), products=products)

    @staticmethod
    async def update_store(store_id: int, store: StorePydanticPatch, db_session: Session):
        update_values = store.dict(exclude={"id"})
        for item in list(update_values):
            if update_values[item] is None:
                update_values.pop(item)

        await StoreManager.update_store(
            product_id=store_id,
            update_values=update_values,
            db_session=db_session
        )

    @staticmethod
    async def add_store(store: StorePydanticCreate, db_session: Session):
        store = await StoreManager.add_store(store=Store(**store.__dict__), db_session=db_session)
        return StorePydantic(**store.__dict__)

    @staticmethod
    async def delete_store_by_id(store_id: int, db_session: Session):
        return await StoreManager.delete_store_by_id(store_id=store_id, db_session=db_session)
