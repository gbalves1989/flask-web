from ..repositories.user_repository import create, find_by_email, update, update_with_avatar
from ..forms.user.register_form import RegisterForm
from ..forms.user.login_form import LoginForm
from ..forms.user.profile_form import ProfileForm
from ..entities.user_entity import UserEntity
from ..entities.profile_entity import ProfileEntity
from ..models.user_model import UserModel
from flask import render_template, redirect, flash, url_for, request, Response
from flask_login import login_user, logout_user
from ..utils.storage import storage_file, storage_delete_file
from werkzeug.datastructures import FileStorage


def create_user(form: RegisterForm) -> Response | None:
    if form.validate_on_submit():
        user_entity: UserEntity = UserEntity(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )

        create(user_entity)
        flash(f'Usuário cadastrado com sucesso', category='success')
        return redirect(url_for('user_routes.page_login'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Erro ao cadastrar o usuário {err}', category='error')

    return render_template('/user/register.html', form=form)


def signin_user(form: LoginForm) -> Response | None:
    if form.validate_on_submit():
        user_db: UserModel = find_by_email(form.email.data)

        if user_db and user_db.verify_password(password_text=form.password.data):
            login_user(user_db)
            flash(f'Logado com sucesso', category='success')
            return redirect(url_for('home_routes.page_home'))

        flash('E-mail ou senha não é válido!', category='error')
        return render_template('/user/login.html', form=form)

    return render_template('/user/login.html', form=form)


def sign_out_user() -> Response:
    logout_user()
    flash('Você fez o logout', category='info')
    return redirect(url_for('user_routes.page_login'))


def update_user(form: ProfileForm) -> Response | str:
    if form.validate_on_submit():
        if request.files['avatar']:
            file: FileStorage = request.files['avatar']
            filename: str = storage_file(file)

            user_db: UserModel = find_by_email(form.email.data)

            if user_db.avatar:
                storage_delete_file(user_db.avatar)

            profile_entity: ProfileEntity = ProfileEntity(
                name=form.name.data,
                avatar=filename
            )

            update_with_avatar(user_db, profile_entity)
            flash(f'Usuário atualizado com sucesso', category='success')
            return redirect(url_for('user_routes.page_profile'))

        user_db: UserModel = find_by_email(form.email.data)
        profile_entity: ProfileEntity = ProfileEntity(
            name=form.name.data
        )

        update(user_db, profile_entity)
        flash(f'Usuário atualizado com sucesso', category='success')
        return redirect(url_for('user_routes.page_profile'))

    return render_template('/user/profile.html', form=form)
