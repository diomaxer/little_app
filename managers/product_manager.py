from sqlalchemy.orm import Session
from src.database.alchemy_models import Product
from src.models.product_models import ProductPydanticCreate


class ProductManager:
    @staticmethod
    async def get_all_products(db_session: Session):
        return db_session.query(Product).all()

    @staticmethod
    async def get_product_by_id(product_id: int, db_session: Session):
        return db_session.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    async def update_product(product_id: int, update_values: dict, db_session: Session):
        db_session.query(Product).filter(Product.id == product_id).update(update_values)
        db_session.commit()

    @staticmethod
    async def add_product(product: Product, db_session: Session):
        db_session.add(product)
        db_session.commit()
        db_session.refresh(product)
        return product

    @staticmethod
    async def delete_product_by_id(product_id: int, db_session: Session):
        db_session.query(Product).filter(Product.id == product_id).delete()
        db_session.commit()

    @staticmethod
    async def get_all_store_products(store_id: int, db_session: Session):
        return db_session.query(Product).filter(Product.store_id == store_id).all()


