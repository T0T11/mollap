from typing import Optional

from core.ProgramadorTasques import ProgramadorTasques


class Mollapp:
    def __init__(self):
        self._programador: Optional[ProgramadorTasques] = None  # anotación de tipo: puede ser None inicialmente

    def set_programador_tasques(self, programador: ProgramadorTasques) -> None:
        self._programador = programador

    def enviar_peticio(self, peticio: str) -> str:
        if self._programador is None:
            raise RuntimeError("Programador de tasques no configurado")
        return self._programador.executar(peticio)
