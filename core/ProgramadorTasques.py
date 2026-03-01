from typing import List
from filtros.Filtre import Filtre
from targets.Target import Target


class ProgramadorTasques:
    def __init__(self, target: Target):
        self._target = target
        self._tasques: List[Filtre] = [] # lista de tareas/filtros a ejecutar antes de delegar al destino

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

if __name__ == "__main__":
    # prueba rápida del programador de tareas con un filtro y un destino de prueba
    from filtros.autenticacio_autorizacio import Autenticacio
    from targets.Vehicle import Vehicle

    target = Vehicle()
    programador = ProgramadorTasques(target)
    programador.set_tasca(Autenticacio())

    usuario = "Francesc"
    programador.executar(usuario)