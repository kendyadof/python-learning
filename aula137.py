# exercício com classes
# 1- crie uma classe carro(nome)
# 2- crie uma classe motor (nome)
# 3- crie uma classe fabricante (nome)
# 4- faça uma ligacao entre carro tem um motor
# obs: um motor pode ser de varios carros
# 5- faca uma ligacao entre carro e um fabricante
# obs um fabricante pode fabricar varios carros
# exiba o nome do carro, motor e fabricante na tela
#  um motor -> varios carros
# um fabricante -> varios carros
# carro-> só tem um fabricante e um motor

# acho q era pra fazer agregação, eu fiz composição

##### Luiz otavio
# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self._motor = None
#         self._fabricante = None

#     @property
#     def motor(self):
#         return self._motor

#     @motor.setter
#     def motor(self, valor):
#         self._motor = valor

#     @property
#     def fabricante(self):
#         return self._fabricante

#     @fabricante.setter
#     def fabricante(self, valor):
#         self._fabricante = valor


# class Motor:
#     def __init__(self, nome):
#         self.nome = nome


# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome


# fusca = Carro('Fusca')
# volkswagen = Fabricante('Volkswagen')
# motor_1_0 = Motor('1.0')
# fusca.fabricante = volkswagen
# fusca.motor = motor_1_0
# print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

# gol = Carro('Gol')
# gol.fabricante = volkswagen
# gol.motor = motor_1_0
# print(gol.nome, gol.fabricante.nome, gol.motor.nome)

# fiat_uno = Carro('Uno')
# fiat = Fabricante('Fiat')
# fiat_uno.fabricante = fiat
# fiat_uno.motor = motor_1_0
# print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

# focus = Carro('Focus Titanium')
# ford = Fabricante('Ford')
# motor_2_0 = Motor('2.0')
# focus.fabricante = ford
# focus.motor = motor_2_0
# print(focus.nome, focus.fabricante.nome, focus.motor.nome)
##### Fim Luiz Otavio

class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = Motor(motor)
        self.fabricante = Fabricante(fabricante)

    def listar_detalhes(self):
        print(self.fabricante.nome, self.nome, self.motor.nome)

    # def __del__(self):
    #     print("Apagando: ", self.fabricante.nome, self.nome, self.motor.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1 = Carro("787B", "Wankel", "Mazda")
# print("### acaba código")
c1.listar_detalhes()

m2 = Motor("13J")
c2 = Carro("787A", m2.nome, "Mazda")

c2.listar_detalhes()

f3 = Fabricante("Volkswagen")
m3 = Motor("Kubel")

c3 = Carro("Nardo", m3.nome, f3.nome)
c3.listar_detalhes()
print(m3.__dict__)