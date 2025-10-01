from .interfaces.elemento_interface import ElementoInterface

# # exemplo 1 sem interface
# class Elemento:
#     def executar(self) -> None:
#         print("Estou execuntanto a classe Elemento")


# exemplo 2 COM INTERFACE
class Elemento(ElementoInterface):
    def executar(self) -> None:
        print("Estou executanto a classe Elemento")
