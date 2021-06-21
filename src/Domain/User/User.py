from route.user import ApiUserCreate, UserSelect
from typing import List
from .CreateUser import CreateUser
from Domain.Repository.User import User as UserRepository
from Domain.User.CreateValidator import CreateValidator
import re
from .CreateValidator import CreateValidator


class User:
    def __init__(self):
        self.repository = UserRepository()

    def all(self) -> List[UserSelect]:
        users = self.repository.all()
        userList = list()
        for user in users:
            userList.append(user.toDict())
        return userList

    def create(self, user: ApiUserCreate) -> int:
        CreateValidator.validate(user)
        creator = CreateUser(user)
        return creator.create()
