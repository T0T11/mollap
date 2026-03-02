from typing import Optional

from core.ProgramadorTasques import ProgramadorTasques


class Mollapp:
    def __init__(self):
        self._programador: Optional[ProgramadorTasques] = None  # anotación de tipo: puede ser None inicialmente

    def set_programador_tasques(self, programador: ProgramadorTasques) -> None: # 
        self._programador = programador

    def enviar_peticio(self, peticio: str) -> str:
        if self._programador is None:
            raise RuntimeError("Programador de tasques no configurado") # raise para indicar que el programador no ha sido configurado
        return self._programador.executar(peticio)

if __name__ == "__main__":
    # prueba rápida de la clase Mollapp con un programador de tareas de prueba
    from filtros.autenticacio_autorizacio import Autenticacio
    from targets.Vehicle import Vehicle

    target = Vehicle()
    programador = ProgramadorTasques(target)
    programador.set_tasca(Autenticacio())

    client = Mollapp()
    client.set_programador_tasques(programador)

    usuario = "Francesc"
    client.enviar_peticio(usuario)