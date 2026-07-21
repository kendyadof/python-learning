# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID # solid: princípios importantes de POO
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  (python não suporta)
# Sobreposição de métodos (override) (python suporta)
from abc import ABC, abstractmethod
class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("Email: enviado...", self.msg)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print("SMS: enviado...", self.msg)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("notificação enviada")
    else:
        print("notificação NAO enviada")

# n = NotificacaoEmail("testando notif email")
# n.enviar()
notificar(NotificacaoEmail("testando email"))
notificar(NotificacaoSMS("testando SMS"))