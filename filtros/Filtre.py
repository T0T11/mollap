from abc import ABC, abstractmethod

class Filtre(ABC):
    @abstractmethod
    def execucio(self, peticio: str) -> None:
        pass
