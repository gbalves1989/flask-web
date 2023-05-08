from ..repositories import category_repository, product_repository
from ..models.product_model import ProductModel
from ..models.category_model import CategoryModel
from typing import List
from flask import render_template


def list_home() -> str:
    categories_db: List[CategoryModel] = category_repository.find_all()
    products_db: List[ProductModel] = product_repository.find_all()
    return render_template('home.html', categories=categories_db, products=products_db)
