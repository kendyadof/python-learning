# Eu deixei a aula 120 como a de Positional-Only Parameters (/) e Keyword-Only Arguments (*).
# como Luiz Otavio criou ela dps, ele deixou como aula145.py
# porém, a aula 120 dele vou deixar como 120b
# Introdução a POO
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = "Luiz" # é uma instância de str
# print(string.upper())
# print(isinstance(string,str))

# PascalCase:
# CriarBaseDeDados
class Pessoa:
    def __init__(self, nome, sobrenome): # o primeiro é sempre self
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Luiz", "Otávio")
# p1.nome = "Luiz"
# p1.sobrenome = "Otávio"
p2 = Pessoa("Maria", "Joana")
# p2.nome = "Luiz"
# p2.sobrenome = "Otávio"
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)