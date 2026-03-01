from targets.Target import Target
class Vehicle(Target):
    def execucio(self, peticio: str) -> None:
        print(f"Vehicle ejecutando: {peticio}")