# aulas 57 e 58 estão no notebook no papai
# desempacotamento em chamadas de métodos e funções

string = "ABCD"
lista = ["Maria", "Helena", "Eduarda"]
tupla = "Python", "é", "legal"


salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

a, b ,c = lista
# print(a, c)

lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
a, b , c, *_ = lista
# print(a, c)

# p =primeiro, ap = ~~ante~~penultimo, u = ultimo
p, b, *_, ap, u = lista
# print(p, u)

#e se quiser imp´rimir as strings em si?
# for nome in lista:
#     print(nome, end=" ")

# isso vai fazer a mesma coisa q o for:
# print(*lista)
# print("Maria", "Helena", 1, 2, 3, "Eduarda")
# print(*string)
# print(*tupla)

print(*salas, sep="\n") # printando a lista dentro de listas
# isso é desempacotamento na chamada das funções