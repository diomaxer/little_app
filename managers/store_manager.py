from sqlalchemy.orm import Session
from database.alchemy_models import Store


class StoreManager:
    @staticmethod
    async def get_all_stores(db_session: Session):
        return db_session.query(Store).all()

    @staticmethod
    async def get_store_by_id(store_id: int, db_session: Session):
        return db_session.query(Store).filter(Store.id == store_id).first()

    @staticmethod
    async def update_store(product_id: int, update_values: dict, db_session: Session):
        db_session.query(Store).filter(Store.id == product_id).update(update_values)
        db_session.commit()

    @staticmethod
    async def add_store(store: Store, db_session: Session):
        db_session.add(store)
        db_session.commit()
        db_session.refresh(store)
        return store

    @staticmethod
    async def delete_store_by_id(store_id: int, db_session: Session):
        db_session.query(Store).filter(Store.id == store_id).delete()
        db_session.commit()
