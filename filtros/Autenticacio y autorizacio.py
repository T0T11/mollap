from filtros.Filtre import Filtre

class Autenticacio(Filtre):
    def execucio(self, peticio: str) -> None:
        print("Autenticando...")

class Autoritzacio(Filtre):
    def execucio(self, peticio: str) -> None:
        print("Autorizando...")
