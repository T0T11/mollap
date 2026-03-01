from targets.Target import Target

class Vehicle(Target):
    def execucio(self, peticio: str) -> str:
        # simular envío de señal inalámbrica para abrir la puerta
        msg = f"Puerta abierta {peticio}!"
        print(msg)
        return msg
    
if __name__ == "__main__":
    # prueba rápida del vehículo
    vehicle = Vehicle()
    usuario = "Javier"
    vehicle.execucio(usuario)