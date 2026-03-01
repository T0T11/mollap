from abc import ABC, abstractmethod
class Target(ABC):
    @abstractmethod
    def execucio(self, peticio: str) -> None:
        pass
