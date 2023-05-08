from ..repositories.product_repository import find_all, create, find_by_id, update, delete
from ..repositories import category_repository
from ..forms.product.create_form import CreateForm
from ..forms.product.update_form import UpdateForm
from ..entities.product_entity import ProductEntity
from ..models.product_model import ProductModel
from ..models.category_model import CategoryModel
from flask import render_template, redirect, flash, url_for, Response
from typing import List


def create_product(form: CreateForm) -> Response | str:
    if form.validate_on_submit():
        product_entity: ProductEntity = ProductEntity(
            name=form.name.data,
            category=form.category.data
        )

        create(product_entity)
        flash('Produto cadastrado com sucesso', category='success')

        return redirect(url_for('product_routes.page_create_product'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar o produto {err}', category='error')

    return render_template('/product/create_product.html', form=form)


def list_products() -> str:
    products_db: List[ProductModel] = find_all()
    return render_template('/product/list_products.html', products=products_db)


def list_categories() -> List[CategoryModel] | None:
    categories_db: List[CategoryModel] = category_repository.find_all()
    return categories_db


def get_product(product_id: int) -> ProductModel | None:
    product_db: ProductModel = find_by_id(product_id)
    return product_db


def update_product(product_id: int, form: UpdateForm) -> Response | None:
    if form.validate_on_submit():
        product_db: ProductModel = find_by_id(product_id)

        product_entity: ProductEntity = ProductEntity(
            name=form.name.data,
            category=product_db.category
        )

        update(product_db, product_entity)
        flash('Produto atualizado com sucesso', category='success')
        return redirect(url_for('product_routes.page_products'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao atualizar o produto {err}', category='error')

    return render_template('/product/edit_product.html', form=form)


def delete_product(product_id: int) -> Response:
    product_db: ProductModel = find_by_id(product_id)
    delete(product_db)
    flash('Produto removido com sucesso', category='success')
    return redirect(url_for('product_routes.page_products'))
