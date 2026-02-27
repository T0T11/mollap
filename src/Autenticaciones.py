from src.Filtro import Filtro

class Autenticacion(Filtro):
    def execution(self, peticion : str) -> str:
        return "Autenticacion exitosa"
    
    
    
class Autorizacion(Filtro):
    def execution(self, peticion : str) -> str:
        return "Autorizacion exitosa"