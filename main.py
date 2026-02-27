from src.Vehiculo import Vehiculo
from src.Autenticaciones import Autenticacion, Autorizacion
from src.ProgramadorTasques import ProgramadorTasques
from src.Mollapp import Mollapp


def main():
    # montar un pequeño escenario siguiendo el diagrama UML
    target = Vehiculo()
    programador = ProgramadorTasques(target)

    # añadir filtros de autenticación y autorización
    programador.set_tasca(Autenticacion())
    programador.set_tasca(Autorizacion())

    client = Mollapp()
    client.set_programador_tasques(programador)

    resultado = client.enviar_peticio("iniciar motor")
    print(resultado)


if __name__ == "__main__":
    main()
