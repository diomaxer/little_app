from sqlalchemy.orm import Session
from src.managers.product_manager import ProductManager
from src.database.alchemy_models import Product
from src.models.product_models import ProductPydanticCreate, ProductPydantic, ProductPydanticPatch


class ProductService:
    @staticmethod
    async def get_all_products(db_session: Session):
        products = await ProductManager.get_all_products(db_session=db_session)
        if not products:
            return None
        return [ProductPydantic(**product.__dict__) for product in products]

    @staticmethod
    async def get_product_by_id(product_id: int, db_session: Session):
        product = await ProductManager.get_product_by_id(product_id=product_id, db_session=db_session)
        if not product:
            return None
        return ProductPydantic(**product.__dict__)

    @staticmethod
    async def update_product(product_id: int, product: ProductPydanticPatch, db_session: Session):
        update_values = product.dict(exclude={"id"})
        for item in list(update_values):
            if update_values[item] is None:
                update_values.pop(item)

        await ProductManager.update_product(
            product_id=product_id,
            update_values=update_values,
            db_session=db_session
        )

    @staticmethod
    async def add_product(product: ProductPydanticCreate, db_session: Session):
        product = await ProductManager.add_product(product=Product(**product.__dict__), db_session=db_session)
        return ProductPydantic(**product.__dict__)

    @staticmethod
    async def delete_product_by_id(product_id: int, db_session: Session):
        return await ProductManager.delete_product_by_id(product_id=product_id, db_session=db_session)
