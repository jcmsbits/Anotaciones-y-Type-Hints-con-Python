# Puedes definir tus propios tipos de datos usando clases

class User:
    def __init__(self, username : str, email : str) -> None :
        self.username : str = username
        self.email : str = email


def make_user(username : str, email : str) -> User :
    return User(username, email)


cody : User = User("Cody", "info@codigofacilito.com")
print(cody.username)
print(cody.email)