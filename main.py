from targets.Vehicle import Vehicle
from filtros.autenticacio_autorizacio import Autenticacio, Autoritzacio
from core.ProgramadorTasques import ProgramadorTasques
from core.Mollapp import Mollapp


def main():
    # montar un pequeño escenario siguiendo el diagrama UML
    target = Vehicle()
    programador = ProgramadorTasques(target)

    # añadir filtros de autenticación y autorización
    programador.set_tasca(Autenticacio())
    programador.set_tasca(Autoritzacio())

    client = Mollapp()
    client.set_programador_tasques(programador)

    usuario = "Francesc"
    # el programador y los filtros ya generan salida en consola; el vehículo
    # también imprime su propio mensaje. no necesitamos imprimir el valor
    # de retorno aquí.
    _ = client.enviar_peticio(usuario)


if __name__ == "__main__":
    main()
