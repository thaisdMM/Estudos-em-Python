from abc import ABC, abstractmethod

# **Contexto:** Uma empresa precisa consolidar a sua lógica de envio de notificações através de diferentes canais (e-mail, SMS, Push Notification), garantindo que cada notificação possa ser enviada por qualquer combinação de canais suportados.

# 1.  **Abstração de Capacidade (Contrato):**
#     * Crie uma classe base abstrata chamada `Notificador` que define o contrato para qualquer sistema de notificação.
#     * Esta classe deve ter um único método abstrato: `enviar(self, mensagem: str)`.


class Notification(ABC):
    """Contract for notification"""

    @abstractmethod
    def send(self, message: str):
        pass


# 2.  **Mixins de Canal (Capacidades Reutilizáveis):**
#     * Crie três classes de tipo **Mixin** que implementam a lógica de envio para canais específicos. Mixins não devem herdar de `Notificador`.
#         * `EmailMixin`: Implementa um método chamado `enviar_email(self, mensagem)`.
#         * `SMSMixin`: Implementa um método chamado `enviar_sms(self, mensagem)`.
#         * `PushMixin`: Implementa um método chamado `enviar_push(self, mensagem)`.
#     * *(Nota: A lógica de envio pode ser simulada com um simples `print()`.)*


class EmailMixin:
    # def __init__(self, message: str):
    #     self._message = message

    def send_email(self, message: str):
        email = message
        if email.strip():
            print(f"Email send successufly: {message}")
            return email
        else:
            raise Exception("Email  invalid.")


class SMSMixin:

    def send_sms(self, message: str):
        sms = message
        if sms.strip():
            print(f"SMS send successufly: {message}")
            return sms
        else:
            raise Exception("SMS  invalid.")


class PushMixin:

    def send_push(self, message: str):
        if message.strip():
            print(f"Push send successufly: {message}")
        else:
            raise Exception("Push  invalid.")


# 3.  **Classe de Serviço (Herança Múltipla):**
#     * Crie uma classe concreta chamada `ServicoDeNotificacao` que **herda de `Notificador`** e utiliza **herança múltipla** para incorporar o **conjunto de Mixins** que desejar (ex: `EmailMixin` e `SMSMixin`).
#     * Implemente o método **`enviar(self, mensagem)`** (obrigatório pelo `Notificador`). Este método deve usar os métodos dos Mixins para enviar a mensagem através de *todos* os canais disponíveis na classe (Polimorfismo).


class NotificationService(Notification):

    def send(self, message: str):
        if message.strip():
            print(f"Sending notification: {message}")
        else:
            raise Exception("Error: the message must be at list 1 caractere.")


class EmailSMSNotification(NotificationService, EmailMixin, SMSMixin):

    def send(self, message: str):
        self.send_email(message)

        self.send_sms(message)


class EmailPushNotification(NotificationService, EmailMixin, PushMixin):

    def send(self, message: str):
        self.send_email(message)
        self.send_push(message)


class SMSPushNotification(NotificationService, SMSMixin, PushMixin):

    def send(self, message: str):
        self.send_sms(message)
        self.send_push(message)


class EmailSMSPushNotification(NotificationService, EmailMixin, SMSMixin, PushMixin):

    def send(self, message: str):
        self.send_email(message)
        self.send_sms(message)
        self.send_push(message)


# 4.  **Teste e Polimorfismo:**
#     * Crie uma lista (ou *tupla*) que contenha instâncias de diferentes configurações de serviço (ex: uma instância que só envia por e-mail/SMS, e outra que envia por todos os três canais).
#     * Itere sobre esta coleção, chame o método `enviar()` em cada objeto, e demonstre que a mensagem é processada corretamente através dos canais suportados por cada instância.

mixin_sms_email = EmailSMSNotification()
mixin_email_push = EmailPushNotification()
mixin_sms_puxh = SMSPushNotification()
mixin_email_sms_push = EmailSMSPushNotification()

mixin_list = [mixin_sms_email, mixin_email_push, mixin_sms_puxh, mixin_email_sms_push]
for mixin in mixin_list:
    print(
        "1 .Call 'NotificationService' that has inheritance from abstract class 'Notification'"
    )
    print("2. Call implemented abstactmethod 'send' from 'NotificationService'...")
    print(
        f"3. Override 'send' from 'NotificationService' method with Call mixin sending method: {type(mixin).__name__}"
    )
    mixin.send("mixin class send method: ")
    print("=-" * 30)
    print()


##
print("TESTES\n")
email1 = EmailMixin()
email1.send_email("Sending email...")

sms1 = SMSMixin()
sms1.send_sms("Sending SMS...")

mixin_sms_email = EmailSMSNotification()
print()
mixin_sms_email.send("You have a email and SMS notification!")
print()
mixin_email_push = EmailPushNotification()
mixin_email_push.send("You have a email and push notification!")
print()
####
# correção GEMINI
import abc
from abc import ABC, abstractmethod


# 1. Abstração de Capacidade (Contrato)
# Define a interface (o contrato) que todas as classes de serviço de notificação devem seguir.
class Notification(ABC):
    """Contrato (Interface) para qualquer sistema de notificação."""

    @abstractmethod
    def send(self, message: str):
        """Método obrigatório que será implementado pelas classes concretas."""
        pass


# 2. Mixins de Canal (Capacidades Reutilizáveis)
# Mixins fornecem o comportamento (a capacidade de envio) e não devem herdar de Notification.
# Eles não devem ter um construtor (__init__) nem manter estado, apenas fornecer métodos.


class EmailMixin:
    """Capacidade de enviar por e-mail."""

    def send_email(self, message: str):
        # Simplificando a validação e removendo o retorno desnecessário para um Mixin de Ação.
        if not message or not message.strip():
            # A simulação deve ser robusta, mas sem lançar a exceção,
            # a menos que isso seja parte do contrato de retorno.
            print("Email: ERRO - Mensagem vazia.")
        else:
            print(f"Email send successfully: {message}")


class SMSMixin:
    """Capacidade de enviar por SMS."""

    def send_sms(self, message: str):
        # Simplificando a lógica. O foco é na composição do comportamento.
        if not message or not message.strip():
            print("SMS: ERRO - Mensagem vazia.")
        else:
            print(f"SMS send successfully: {message}")


class PushMixin:
    """Capacidade de enviar Push Notification."""

    def send_push(self, message: str):
        if not message or not message.strip():
            print("Push: ERRO - Mensagem vazia.")
        else:
            print(f"Push send successfully: {message}")


# 3. Classe de Serviço (Herança Múltipla)
# Conforme o enunciado, ServicoDeNotificacao é a classe concreta que une o Contrato (Notification)
# e as Capacidades (Mixins) via Herança Múltipla.


# Esta é a classe ServicoDeNotificacao que o enunciado pede.
# Ela herda diretamente de Notification (o contrato) e dos Mixins.
class NotificationService(Notification, EmailMixin, SMSMixin):
    """
    Serviço concreto que herda o contrato (Notification) e as capacidades (Mixins).
    Esta classe cumpre o Requisito 3 do enunciado.
    """

    def send(self, message: str):
        """Implementa o método obrigatório 'send' usando as capacidades dos Mixins."""
        print(f"\n--- Iniciando Serviço: {type(self).__name__} ---")

        # O self.send_email é herdado do EmailMixin
        self.send_email(message)

        # O self.send_sms é herdado do SMSMixin
        self.send_sms(message)


# Classes Adicionais de Serviço (Para o Teste de Polimorfismo no Requisito 4)
# Estas classes seguem a mesma lógica de Herança Múltipla para criar outras combinações.


class EmailPushService(Notification, EmailMixin, PushMixin):
    """Serviço que combina Email e Push."""

    def send(self, message: str):
        print(f"\n--- Iniciando Serviço: {type(self).__name__} ---")
        self.send_email(message)
        self.send_push(message)


class AllChannelsService(Notification, EmailMixin, SMSMixin, PushMixin):
    """Serviço que combina Email, SMS e Push."""

    def send(self, message: str):
        print(f"\n--- Iniciando Serviço: {type(self).__name__} ---")
        self.send_email(message)
        self.send_sms(message)
        self.send_push(message)


# 4. Teste e Polimorfismo
# Demonstra que podemos tratar diferentes classes de serviço (com diferentes combinações de canais)
# de forma uniforme, chamando apenas o método 'send', sem saber o tipo exato do objeto.

# 4a. Criação das instâncias
servico_email_sms = NotificationService()  # Corresponde à classe pedida no Requisito 3
servico_email_push = EmailPushService()
servico_todos_canais = AllChannelsService()

# 4b. Criação da coleção (lista)
servicos = [
    servico_email_sms,
    servico_email_push,
    servico_todos_canais,
]

# 4c. Iteração e demonstração do Polimorfismo
print("==============================================")
print("TESTE DE POLIMORFISMO (REQUISITO 4)")
print("==============================================")

for servico in servicos:
    # A chamada é a mesma para todos os objetos, mas o comportamento (os canais de envio) é diferente.
    # Esta é a demonstração do Polimorfismo.
    servico.send("Mensagem polimórfica de teste: Promoção de Natal!")
    print("\n----------------------------------------------")

# Demonstração de uma chamada para uma instância que não funciona (exceção se a mensagem for vazia)
try:
    print("\nTeste de Mensagem Vazia:")
    servico_email_sms.send("")
except Exception as e:
    # Captura da exceção para evitar a parada do programa (caso tivéssemos implementado raises nos mixins)
    # Com a lógica atual de print de erro, isso não será acionado, mas é boa prática.
    print(f"Um erro foi capturado (esperado em ambiente real): {e}")
