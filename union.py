from typing import Union, List

# Para especificar que una variables puede guardar diferentes tipos de datos usamos Union
username : Union[str, None]


# Si puede devolver n tipo de datos lo puedes poner con Union[int, str, None, float, ...]

# def average(numbers: List[int]) -> Union[None, float] :

# En versiones mas modernas ( > 3.9) de Python puedes especificar varios tipos con el caracter pipe
def average(numbers: List[int]) -> None | float :
    if len(numbers) == 0 :
        return None
    
    return sum(numbers) / len(numbers)


numbers = []
# result : Union[None, float] = average(numbers)

result : None | float = average(numbers)
print(result)