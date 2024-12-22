from typing import Literal

# Con el tipo de anotacion Literal podemos definir una cantidad limitada de opciones
# se puede escoger cualquier opción que se encuentre del listado
# Se encuentra a partir de la 3.11 de python
# funciona Enum 

def set_background_color(color : Literal["red", "green", "blue", "white", "black"]) :
    pass

def make_user(username : str, email : str, gender : Literal["M", "F"]) :
    pass

def open_handler(file : str, mode: Literal["r", "rb", "w", "wb"]) :
    pass