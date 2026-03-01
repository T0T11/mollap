from filtros.Filtre import Filtre

class Autenticacio(Filtre):
    def execucio(self, peticio: str) -> None:
        # el sistema está en periodo de pruebas, todos tienen acceso
        # cadena solo ASCII para evitar problemas de codificación
        print(f"Autenticacion OK para {peticio}")

class Autoritzacio(Filtre):
    def execucio(self, peticio: str) -> None:
        # de nuevo, aún no se necesita lógica real
        print(f"Autorizacion OK para {peticio}")
