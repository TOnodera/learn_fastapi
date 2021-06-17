from route.route import UserCreate
from Domain.Repository.User import User as UserRepository


class CreateUser:

    def __init__(self, user: UserCreate):
        self.name = user.name
        self.email = user.email
        self.repository = UserRepository()

    def create(self) -> int:
        return self.repository.create(self.name, self.email)
