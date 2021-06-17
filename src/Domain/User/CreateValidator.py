from Domain.Exception.DomainException import DomainException
from route.route import UserCreate
from .UserValidator import UserValidator
import re


class CreateValidator(UserValidator):

    @classmethod
    def validate(cls, user: UserCreate):

        if len(user.name) < cls.userNameMinSize:
            raise DomainException(
                "ユーザー名は{}文字以上で入力して下さい。".format(cls.userNameMinSize))

        if cls.userNameMaxSize < len(user.name):
            raise DomainException(
                "ユーザー名は{}文字以内で入力して下さい。".format(cls.userNameMaxSize))

        if not re.match(cls.emailPattern, user.email) or cls.emailMaxSize < len(user.email):
            raise DomainException("正しい形式のメールアドレスを入力して下さい。")
