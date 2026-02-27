from typing import List, Optional

from src.Filtro import Filtro
from src.Target import Target

class Tasques:
    """Representa un conjunto de filtros y un target final.

    Sigue el diseño mostrado en el diagrama UML.
    """

    def __init__(self) -> None:
        # lista de filtros que se ejecutarán en orden
        self.tasques: List[Filtro] = []
        # el objetivo al que se delega la petición al final
        self.target: Optional[Target] = None

    def get_tasques(self) -> List[Filtro]:
        return self.tasques

    def get_target(self) -> Optional[Target]:
        return self.target

    def afegir_tasca(self, filtre: Filtro) -> None:
        """Añade un filtro a la cadena."""
        self.tasques.append(filtre)

    def set_target(self, target: Target) -> None:
        """Configura el target que manejará la petición tras los filtros."""
        self.target = target

    def execution(self, peticion: str) -> str:
        """Ejecuta todos los filtros y, si hay un target, le reenvía la petición.

        Devuelve la cadena resultante tras pasar por cada elemento.
        """
        resultado = peticion
        for f in self.tasques:
            resultado = f.execution(resultado)
        if self.target is not None:
            resultado = self.target.execution(resultado)
        return resultado
