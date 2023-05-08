from ..entities.product_entity import ProductEntity
from ..models.product_model import ProductModel
from typing import List
from web import db


def create(entity: ProductEntity) -> None:
    product_db: ProductModel = ProductModel(
        name=entity.name,
        category=entity.category
    )

    db.session.add(product_db)
    db.session.commit()


def find_all() -> List[ProductModel] | None:
    products_db: List[ProductModel] = ProductModel.query.all()
    return products_db


def find_by_id(product_id: int) -> ProductModel | None:
    product_db: ProductModel = ProductModel.query.filter_by(id=product_id).first()
    return product_db


def update(product_db: ProductModel, product_entity: ProductEntity) -> None:
    product_db.name = product_entity.name
    product_db.category = product_entity.category
    db.session.commit()


def delete(product_db: ProductModel) -> None:
    db.session.delete(product_db)
    db.session.commit()
