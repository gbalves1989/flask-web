from web import db
from ..entities.category_entity import CategoryEntity
from ..models.category_model import CategoryModel
from typing import List


def create(entity: CategoryEntity) -> None:
    category_db: CategoryModel = CategoryModel(
        name=entity.name
    )

    db.session.add(category_db)
    db.session.commit()


def find_by_id(category_id: int) -> CategoryModel | None:
    category_db: CategoryModel = CategoryModel.query.filter_by(id=category_id).first()
    return category_db


def find_all() -> List[CategoryModel] | None:
    categories_db: List[CategoryModel] = CategoryModel.query.all()
    return categories_db


def update(category_db: CategoryModel, category_entity: CategoryEntity) -> None:
    category_db.name = category_entity.name
    db.session.commit()


def delete(category_db: CategoryModel) -> None:
    db.session.delete(category_db)
    db.session.commit()
