from route.user import ApiUserCreate
from Domain.Repository.User import User as UserRepository


class CreateUser:

    def __init__(self, user: ApiUserCreate):
        self.user = user
        self.repository = UserRepository()

    def create(self) -> int:
        return self.repository.create(self.user)
