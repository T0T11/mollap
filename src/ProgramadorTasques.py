from typing import Optional

from src.Tasques import Tasques
from src.Filtro import Filtro
from src.Target import Target


class ProgramadorTasques:
    

    def __init__(self, target: Target) -> None:
        self._target = target
        self._tasques = Tasques()
        self._tasques.set_target(target)

    def get_tasques(self) -> Tasques:
        return self._tasques

    def set_tasca(self, filtre: Filtro) -> None:
        
        self._tasques.afegir_tasca(filtre)

    def executar_tasques(self, peticion: str) -> str:
        
        return self._tasques.execution(peticion)
