class UserValidator:
    userNameMinSize = 2
    userNameMaxSize = 100
    emailMaxSize = 255
    emailPattern = '(^[a-zA-Z0-9_.+-]+[^.]@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
