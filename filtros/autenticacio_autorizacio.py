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


if __name__ == "__main__":
    # prueba rápida de los filtros
    autenticacio = Autenticacio()
    autoritzacio = Autoritzacio()

    usuario2 = "Alice"
    autenticacio.execucio(usuario2)
    autoritzacio.execucio(usuario2)
    usuario = "Francesc"
    autenticacio.execucio(usuario)
    autoritzacio.execucio(usuario)