from typing import Dict, List, Tuple

numbers : List[int] = [1, 2, 3]
names : Tuple[str, str] = ("user1", "user2")
scores : Dict[str, int] = {"user1" : 100, "user2" : 70 }

print(numbers)
print(names)
print(scores)


# Esto funciona
setting : tuple = (True, 3306, "root")

# Pero si queremos ser mas especifico podemos usar la clase Tuple de typing

setting : Tuple[bool, int, str] = (True, 3306, "root")

