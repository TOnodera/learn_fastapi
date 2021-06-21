from database.models import User as UserModel
from Domain.Repository.Repository import Repository
from route.user import ApiUserCreate


class User(Repository):

    def __init__(self):
        super().__init__()

    def all(self):
        return self.connection.query(UserModel).all()

    def get(self, user_id: int):
        return self.connection.query(UserModel).get(user_id)

    def create(self, user: ApiUserCreate):
        orm = UserModel()
        orm.name = user.name
        orm.email = user.email
        orm.memo = user.memo
        orm.image = user.image
        self.connection.add(orm)
        self.connection.commit()
        return orm.id
