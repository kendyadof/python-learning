# métodos em instâncias de classes python
# hard coded = algo q foi escrto diretamente no código
class Carro:
    def __init__(self, nome): # -> None # init sempre retorna None
        self.nome = nome

    def acelerar(self): #tem q passar self tb
        print(f"{self.nome} está acelerando...")

fusca = Carro("Fusca")
# print(fusca.nome)
fusca.acelerar()
# fusca.nome = "Fusca"
celta = Carro(nome="Celta")
# print(celta.nome)
celta.acelerar()
# método é uma função que está dentro da classe
# acho q em java self era this