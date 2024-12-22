# Any & Optional
from typing import Any, Optional

# Any se usa cuando no se tiene conocimientos del tipo de variables con la cual se trabaja
# se puede especificar cualquier tipo de datos con el
# No es muy recomendable usarla por temas de ambiguedad y poca legibilidad en el código

def test(something : Any ) -> Any :
    return something

# Optional se usa para los parametros de las funciones que pueden ser opcionales porque tienen valores
# por defecto

def foo(param : Optional[int] = 10) -> int:
    return param