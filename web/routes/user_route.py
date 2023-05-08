from flask import Blueprint, render_template
from ..forms.user.register_form import RegisterForm
from ..forms.user.login_form import LoginForm
from ..forms.user.profile_form import ProfileForm
from ..services.user_service import create_user, signin_user, sign_out_user, update_user
from flask_login import current_user, login_required


user_blueprint = Blueprint('user_routes', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def page_register():
    form: RegisterForm = RegisterForm()
    return create_user(form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def page_login():
    form: LoginForm = LoginForm()
    return signin_user(form)


@user_blueprint.route('/logout')
@login_required
def page_logout():
    return sign_out_user()


@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def page_profile():
    form: ProfileForm = ProfileForm()
    form.avatar.data = current_user.avatar
    form.name.data = current_user.name
    form.email.data = current_user.email

    return render_template('/user/profile.html', form=form)


@user_blueprint.route('/profile/update', methods=['GET', 'POST'])
@login_required
def page_profile_update():
    form: ProfileForm = ProfileForm()
    return update_user(form)
