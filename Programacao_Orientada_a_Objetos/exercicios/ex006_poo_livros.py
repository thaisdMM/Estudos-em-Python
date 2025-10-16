# ###  Sistema de Gestão de Livros com Propriedades e Encapsulamento**

# **Objetivo:** Criar uma classe que represente um livro, implementando **Encapsulamento** e utilizando **Propriedades** para garantir que os dados sejam válidos ao serem acessados ou modificados.


class Livro:
    def __init__(self, title: str, author: str, number_of_pages: int):
        self._title = title
        self._author = author
        # chama o setter para validar
        self.number_of_pages = number_of_pages

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def number_of_pages(self) -> int:
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, new_number_of_pages) -> int:

        if isinstance(new_number_of_pages, int) and new_number_of_pages > 0:
            self._number_of_pages = new_number_of_pages
        else:
            raise ValueError("Number of pages must be integer and positive.")

    def to_dict(self) -> dict:
        return {
            "title": self._title,
            "author": self._author,
            "number_of_pages": self._number_of_pages,
        }


dom_casmurro = Livro("Dom Casmurro", "Machado de Assis", 150)
print(dom_casmurro.author)
print(dom_casmurro.number_of_pages)
print(dom_casmurro.title)
print(dom_casmurro.to_dict())

print(f"New number of pages: {dom_casmurro.number_of_pages}")
# Teste de Escrita (agora funciona corretamente)
dom_casmurro.number_of_pages = 180
print(f"Novo número de páginas (Escrita Correta): {dom_casmurro.number_of_pages}")


# Teste de Validação (deve levantar um erro)
try:
    dom_casmurro.number_of_pages = -5
except ValueError as e:
    print(f"\nTeste de Erro (Sucesso): {e}")

try:
    dom_casmurro.number_of_pages = 10.5
except ValueError as e:
    print(f"Teste de Erro (Sucesso): {e}")
