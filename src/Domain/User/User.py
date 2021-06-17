from route.route import UserCreate, UserSelect
from typing import List
from .CreateUser import CreateUser
from Domain.Repository.User import User as UserRepository


class User:
    def __init__(self):
        self.repository = UserRepository()

    def all(self) -> List[UserSelect]:
        users = self.repository.all()
        userList = list()
        for user in users:
            userList.append(user.toDict())
        return userList

    def create(self, user: UserCreate) -> int:
        creator = CreateUser(user)
        return creator.create()
