# Abstraction
# Reduce complexity by hiding unnecessary details.

# Abstração é o princípio da POO que consiste em esconder detalhes complexos de implementação e expor apenas o necessário para o uso de um objeto. Ela permite que você foque no que o objeto faz, e não em como ele faz.

# Para que serve?
# Simplificar o uso de objetos complexos.
# Reduzir acoplamento, ou seja, a dependência entre partes do código.
# Aumentar a reutilização e a manutenibilidade do código.
# Organizar o sistema em níveis de hierarquia e responsabilidade clara.
# Facilitar testes e alterações sem quebrar outras partes do sistema.

# Como funciona?
# Na prática, usamos a abstração por meio de:

# Classes abstratas (com métodos que não têm implementação completa).
# Interfaces (em linguagens como Java; em Python usamos classes base com métodos abstratos).
# Uso de métodos públicos e ocultação da lógica interna.


class EmailService:

    def _connect(self):
        print("connecting to email server")

    def _authenticate(self):
        print("Autenticating...")

    # essa tem que ser pública, pois é a que o usário se importa,
    # as classes protegidas nesse exemplo não interessam ao usuário
    def send_email(self):
        self._connect()
        self._authenticate
        print("Sending email...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")


email = EmailService()
email.send_email()
