from abc import ABC, abstractmethod


# -------------------------
# 1) Contrato (Abstração)
# -------------------------
class Notificador(ABC):
    """
    Contrato: todo notificador deve implementar o metodo enviar.
    Método: enviar(mensagem: str) ->deve lançar exceção em caso de erro,
    ou retornar um relatório/valor que indique sucesso.
    """

    @abstractmethod
    def enviar(self, mensagem: str):
        raise NotImplementedError


# -------------------------
# 2) Mixins de canal
# -------------------------


class EmailMixin:
    "Mixin que tem capacidade de enviar mensagem por e-email"

    def enviar_email(self, mensagem: str):
        if not mensagem or not mensagem.strip():
            raise ValueError("Email inválido: mensagem vazia.")
        print(f"[Email] envidado: {mensagem}")
        return {"canal": "email", "status": "sucesso"}


class SMSMixin:
    "Mixin que tem capacidade de enviar mensagem por SMS"

    def enviar_sms(self, mensagem: str):
        if not mensagem or not mensagem.strip():
            raise ValueError("SMS inválida: mensagem vazia")
        print(f"[SMS] enviado:  {mensagem}")
        return {"canal": "SMS", "status": "sucesso"}


class PushMixin:
    "Mixin que tem capacidade de enviar mensagem por push"

    def enviar_push(self, mensagem: str):
        if not mensagem or not mensagem.strip():
            raise ValueError("Push inválida: mensagem vazia")
        print(f"[Push] enviado:  {mensagem}")
        return {"canal": "push", "status": "sucesso"}


# -------------------------------------------------
# 3) Servico de notificação (herda de Notificador)
# -------------------------------------------------
class ServicoDeNotificacao(Notificador):
    """
    Implementa o método 'enviar' do contrato.
    Estratégia: tenta chamar, na ordem, os métodos de canal conhecidos
    (enviar_email, enviar_sms, enviar_push) somente se eles existirem na instância.
    - Acumula um relatório por canal (sucesso/erro).
    - Não exige que cada combinação sobrescreva 'enviar' — aproveita herança múltipla.
    """

    # Ordem em que os canais serão tentados (padrão do exercício).
    _CANAL_METODOS = ("enviar_email", "enviar_sms", "enviar_push")

    def enviar(self, mensagem: str):
        if not mensagem or not mensagem.strip():
            raise ValueError("Erro: não é possivel enviar mensagem vazia.")

        resultados = []
        for metodo_nome in self._CANAL_METODOS:
            # chama apenas se o método existir nesta instância (herdado via mixin)
            # getattr(objeto, "nome_do_atributo", valor_padrao): tenta pegar o atributo nome_do_atributo do objeto.
            # Se existir, retorna esse atributo (pode ser um método ou um valor).
            # Se não existir, retorna valor_padrao (geralmente None).
            metodo = getattr(self, metodo_nome, None)
            # verifica se o que foi recuperado é chamável (um método ou função), ou seja: se é seguro fazer metodo(...)
            # Por que: getattr pode devolver muitas coisas (um número, None, um método). callable garante que é mesmo um método que podemos executar.
            if callable(metodo):
                try:
                    # tenta executar o método do mixin — por exemplo, chama self.enviar_email(mensagem)
                    resultado = metodo(mensagem)
                    # normaliza formato do resultado para o relatório
                    if isinstance(resultado, dict):
                        resultados.append(resultado)
                    else:
                        # DEFENSIVO: se o mixin não retornou um dicionário (por exemplo retornou None ou True), o código normaliza o resultado e adiciona um dicionário padrão dizendo que o canal teve sucesso.
                        resultados.append({"canal": metodo_nome, "status": "Sucesso"})

                except Exception as exc:
                    # registra falha nesse canal e continua nos demais
                    resultados.append(
                        {"canal": metodo_nome, "status": "erro", "erro": str(exc)}
                    )

            else:
                # canal não suportado pela combinação atual(simplemente pula)
                resultados.append({"canal": metodo_nome, "status": "não_suportado"})

        return resultados


# -------------------------------------------------------------------
# 4) Classes concretas que combinam ServicoDeNotificacao + mixins
#    (exemplos de combinações via herança múltipla)
# -------------------------------------------------------------------
class NotificacaoEmailSMS(ServicoDeNotificacao, EmailMixin, SMSMixin):
    """Suporta Email + SMS (não precisa sobrescrever 'enviar')."""

    pass


class NotificacaoEmailPush(ServicoDeNotificacao, EmailMixin, PushMixin):
    """Suporta Email + Push."""

    pass


class NotificacaoSMSPush(ServicoDeNotificacao, SMSMixin, PushMixin):
    """Suporta SMS + Push."""

    pass


class NotificacaoEmailSMSPush(ServicoDeNotificacao, EmailMixin, SMSMixin, PushMixin):
    """Suporta Email + SMS + Push."""

    pass


# 4.  **Teste e Polimorfismo:**
#     * Crie uma lista (ou *tupla*) que contenha instâncias de diferentes configurações de serviço (ex: uma instância que só envia por e-mail/SMS, e outra que envia por todos os três canais).
#     * Itere sobre esta coleção, chame o método `enviar()` em cada objeto, e demonstre que a mensagem é processada corretamente através dos canais suportados por cada instância.

# -------------------------
# 5) Demonstração / Testes
# -------------------------

if __name__ == "__main__":
    instancias = [
        NotificacaoEmailSMS(),
        NotificacaoEmailPush(),
        NotificacaoSMSPush(),
        NotificacaoEmailSMSPush(),
    ]

    mensagem = "Teste: você recebeu uma nova notificação."

    for instancia in instancias:
        print(f"\n>>> Enviando com {type(instancia).__name__} <<<")
        relatorio = instancia.enviar(mensagem)
        print(f"Relatório do envio das mensagens: {relatorio}")

    # Teste isolado dos mixins (útil para aprendizado; aceitável em exercício)
    print("\n--- Testes isolados de mixins ---")
    email = EmailMixin()
    print("EmailMixin:", email.enviar_email("Teste de email"))

    sms = SMSMixin()
    print("SMSMixin:", sms.enviar_sms("Teste de SMS"))

    push = PushMixin()
    print("PushMixin:", push.enviar_push("Teste de push"))
