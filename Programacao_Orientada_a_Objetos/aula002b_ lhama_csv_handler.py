# Classe para lidar com arquvos csv
class CsvHandler:
    # método constutor
    def __init__(self, directory) -> None:
        # atributo
        self.dir = directory

    # método - ação
    def insert_data_in_csv(self, data):
        print(f"Inserindo{data} em {self.dir}")

    # método - ação
    def read_data(self):
        print(f"Read data in {self.dir}")


# passa o caminho no método construtor: directory e fica armazenado no atributo
csv_handle = CsvHandler("o/caminho/do/diretorio/.csv")

# os outros métodos pode usar a "informação" que está no método construtor
csv_handle.read_data()
## output:
## Read data in o/caminho/do/diretorio/.csv
