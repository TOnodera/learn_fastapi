from database.models import User as UserModel
from database.config import connection


class User:
    def all(self):
        return connection.query(UserModel).all()

    def create(self, name: str, email: str):
        orm = UserModel()
        orm.name = name
        orm.email = email
        connection.add(orm)
        connection.commit()
        return orm.id
