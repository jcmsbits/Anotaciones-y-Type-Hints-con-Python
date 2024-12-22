from typing import List

# Con tipado el código se lee mucho mejor y deja poco espacio para las ambiguedades
def average(numbers : List[int]) -> float:
    return sum(numbers) / len(numbers)


scores : List[int] = [10, 10, 9, 8, 8 , 8]
result: float = average(scores)

print(result)

# Para evitar ambiguedad especificamos el tipo 
def _sum(number_1 : int, number_2 : int) -> int:
    return number_1 + number_2

result = _sum(10,20)

print(result)

result = _sum("Cody", "Saluda")

print(result)