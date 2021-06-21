from route.user import UserCreate
from Domain.Repository.User import User as UserRepository


class CreateUser:

    def __init__(self, user: UserCreate):
        self.user = user
        self.repository = UserRepository()

    def create(self) -> int:
        return self.repository.create(self.user)
