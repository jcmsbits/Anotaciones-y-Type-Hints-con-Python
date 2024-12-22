username : str = "cody"
altura : float = 1.6
edad : int = 10
activo : bool = True

print(username, altura, edad, activo)

# Tambien podemos declarar la variable y el tipo antes de asignarlo

username : str
altura : float
edad : int
activo : bool

# Y podemos asignarle un valor no definido con anterioridad

username = 100_000
altura = 1.6
print(username, altura)

# Como programadores deberiamos respetar las reglas porque python no va a penalizar lo que asignemos

# Las variables None nos permite definir la ausencia de algún valor

username : None = None

print(username)