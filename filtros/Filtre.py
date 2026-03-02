from abc import ABC, abstractmethod # ABC es para definir clases abstractas, abstractmethod es para definir métodos abstractos  

class Filtre(ABC):
    @abstractmethod
    def execucio(self, peticio: str) -> None:  # significa que retorna nada 
        pass
