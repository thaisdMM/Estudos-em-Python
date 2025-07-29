## @PROPERTY: Outra forma do getter e setter

# o decorador @property:
# O @property é uma forma idiomática e Pythonica de encapsular atributos de uma classe, permitindo que você:

# Acesse atributos como se fossem variáveis públicas (obj.nome)
# Mas, por trás, tenha lógica de métodos privados ou controlados, como validações, cálculos ou transformações

# Vantagem real do @property:

# Você pode começar com um atributo público simples.
# Depois, se precisar de lógica, transforma em @property, sem mudar o código externo.

# Críticas

# Você não vê claramente que está executando lógica, pois parece um acesso simples de variável.
# Pode haver efeitos colaterais inesperados escondidos atrás de um acesso “inocente”.

# Em Python moderno e profissional:

# Use @property para encapsular comportamento leve com aparência de atributo.
# Evite lógica pesada ou efeitos colaterais dentro de @property – nesse caso, use um método explícito.

# Se você precisar de lógica de validação ou transformação futura, @property é a melhor escolha, pois preserva a interface.
# Para dados claramente computados ou que envolvem ações, prefira métodos normais, para deixar claro que há um processo.


class MinhaClasse:
    def __init__(self) -> None:
        # atributo privado
        self.__valor = None
        self.__elemento = None

    # método setter - público, mas interage com um atributo privado
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor

    # método getter - público, mas interage com um atributo privado
    @property  # mascara a classe como se fosse atributo?
    def getter_valor(self) -> int:
        return self.__valor


# está chamando como se fosse um método normal, mas na verdade é getter com uso do decorador @property
my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor)
