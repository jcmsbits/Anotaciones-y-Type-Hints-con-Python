# Con NamedTuple hacemos inmutable el objeto, como si fuera una tupla
# con sus diferentes variables y tipos de cada una
from typing import NamedTuple


class DataseBaseSetting(NamedTuple) :
    username : str
    password : str
    port : int
    database : str

database_config = DataseBaseSetting(
    "root",
    "password123",
    3306,
    "codigofacilito"
)

print(database_config)
print(database_config.username)
print(database_config.password)
print(database_config.port)
print(database_config.database)

