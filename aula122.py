# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome): # self é um nome de convenção, poderia ser nomeado madurinha, mas funciona
        self.nome = nome

    def acelerar(self): # self aqui tb poderia ser madurinha2
        print(f"{self.nome} está acelerando...")

fusca = Carro("Fusca")
Carro.acelerar(fusca)
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome="Celta")
Carro.acelerar(celta)
print(celta.nome)
celta.acelerar()