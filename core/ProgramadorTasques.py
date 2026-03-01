from typing import List
from filtros.Filtre import Filtre
from targets.Target import Target


class ProgramadorTasques:
    def __init__(self, target: Target):
        self._target = target
        self._tasques: List[Filtre] = []

    def set_tasca(self, tasca: Filtre) -> None:
        """Añade un filtro/tarea a ejecutar antes de delegar al destino."""
        self._tasques.append(tasca)

    def executar(self, peticio: str) -> str:
        """Ejecuta todas las tareas en orden y finalmente delega la peticion al destino.

        Cada tarea puede producir efectos secundarios (impresiones), y el valor
        retornado por el destino se propaga al llamador.
        """
        for tasca in self._tasques:
            tasca.execucio(peticio)
        return self._target.execucio(peticio)
