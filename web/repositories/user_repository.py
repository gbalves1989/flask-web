from web import db
from ..entities.user_entity import UserEntity
from ..entities.profile_entity import ProfileEntity
from ..models.user_model import UserModel


def create(entity: UserEntity) -> None:
    user_db: UserModel = UserModel(
        name=entity.name,
        email=entity.email,
        password_hash=entity.password
    )

    db.session.add(user_db)
    db.session.commit()


def find_by_email(email: str) -> UserModel | None:
    user_db: UserModel = UserModel.query.filter_by(email=email).first()
    return user_db


def update_with_avatar(user_db: UserModel, user_entity: ProfileEntity) -> None:
    user_db.name = user_entity.name
    user_db.avatar = user_entity.avatar
    db.session.commit()


def update(user_db: UserModel, user_entity: ProfileEntity) -> None:
    user_db.name = user_entity.name
    db.session.commit()
