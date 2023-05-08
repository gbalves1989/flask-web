from ..repositories.category_repository import create, find_by_id, find_all, delete, update
from ..forms.category.create_update_form import CreateUpdateForm
from ..entities.category_entity import CategoryEntity
from ..models.category_model import CategoryModel
from flask import render_template, redirect, flash, url_for, Response
from typing import List


def create_category(form: CreateUpdateForm) -> Response | str:
    if form.validate_on_submit():
        category_entity: CategoryEntity = CategoryEntity(
            name=form.name.data
        )

        create(category_entity)
        flash('Categoria cadastrada com sucesso', category='success')
        return redirect(url_for('category_routes.page_create_category'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar a categoria {err}', category='error')

    return render_template('/category/create_category.html', form=form)


def list_categories() -> str:
    categories_db: List[CategoryModel] = find_all()
    return render_template('/category/list_categories.html', categories=categories_db)


def get_category(category_id: int) -> CategoryModel | None:
    category_db: CategoryModel = find_by_id(category_id)
    return category_db


def update_category(category_id: int, form: CreateUpdateForm) -> Response | str:
    if form.validate_on_submit():
        category_db: CategoryModel = find_by_id(category_id)

        category_entity: CategoryEntity = CategoryEntity(
            name=form.name.data
        )

        update(category_db, category_entity)
        flash('Categoria atualizada com sucesso', category='success')
        return redirect(url_for('category_routes.page_categories'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao atualizar a categoria {err}', category='error')

    return render_template('/category/edit_category.html', form=form)


def delete_category(category_id: int) -> Response:
    category_db: CategoryModel = find_by_id(category_id)
    delete(category_db)
    flash('Categoria removida com sucesso', category='success')
    return redirect(url_for('category_routes.page_categories'))
