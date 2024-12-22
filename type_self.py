from typing import Self
# Self  > 3.11 de python
# Mediante esta anotación seremos capaces de indicar que nuestros
# métodos serán capaces de regresar objetos del mismo tipo de la clase
# ya sea la misma instancia u / o otro objeto nuevo pero del mismo tipo de la clase

class User:

    def __init__(self, username : str, email : str) -> None :
        self.username : str = username
        self.email : str = email

    def copy(self) -> Self:
        return User(self.username, self.email)

    def get_user(self):
        return self

    def __str__(self) -> str:
        return f"{self.username} - {self.email}"


cody = User("cody", "info@codigofacilito.com")
cody2 = cody.get_user()
cody_copy = cody.copy()
print("Codycopy", cody_copy, "ID: ", id(cody_copy))
print("Copy", cody, "ID: ", id(cody))
print("Cody2", cody2, "ID: ", id(cody2))


 