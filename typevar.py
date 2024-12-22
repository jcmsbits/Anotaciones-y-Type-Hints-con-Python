# TypeVar 
# Este es un poco más complejo porque son de tipos mas génerico
# y no sabemos cuales son
# Mientras que Any significa que la variable puede ser cualquier tipo
# que se deshabilita la verificación de tipos para esa variable
from typing import List, TypeVar, Tuple, Dict

# Como no sabemos que tipo de datos vamos a trabajar por convección
# ponemos T
T = TypeVar("T")
Collection = TypeVar("Collection", List, Tuple, Dict)

def first_element(collection : List[T]) ->  T | None:
    """ Retornar el primer elemento de una colección """

    if len(collection) == 0:
        return None
    
    return collection[0]

print(
    first_element([1,2,3,4,5])
)

print(
    first_element(["User1", "User2", "User3"])
)


Number = TypeVar("Number", int, float)

def double(number : Number) -> Number :
    return number * 2

result: Number = double(10)
print(result)