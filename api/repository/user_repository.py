from sqlalchemy import select

from ..config.extensions import db
from ..model.user import User


class UserRepository:
    """User repository class"""

    def get_all(self):
        return db.session.scalars(select(User)).all()

    def get_by_id(self, user_id):
        return db.session.get(User, user_id)

    def add(self, user):
        db.session.add(user)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
