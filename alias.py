from typing import Tuple, Union

# Los alias permiten reducir el código asignandole un nombre a los tipos y
# tambien hacer el codigo mas legibles

ConnectionType = Tuple[str, str, str]
UserIdorNone = int | None

def database_connection(connection : ConnectionType) -> ConnectionType | None :

    if connection[0] == "root" :
        return None
    
    return connection


connection : ConnectionType = ("root", "codigofacilito", 3306)
print(database_connection(connection))