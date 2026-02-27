from src.Target import Target

class Vehiculo(Target):
    """Un target concreto que representa un vehículo."""

    def execution(self, peticion: str) -> str:
        return "Ejecutando la petición en el vehículo"