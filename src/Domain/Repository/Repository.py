from database.config import connection


class Repository:
    def __init__(self):
        self.connection = connection
