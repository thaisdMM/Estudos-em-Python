from .interfaces.elemento_interface import ElementoInterface


# exemplo 2/3 COM mais uma INTERFACE
class Elemento2(ElementoInterface):
    def executar(self) -> None:
        print("Estou executanto a classe Elemento 2")
