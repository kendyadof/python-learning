"""
exercicio
exiba os indices da lista
usando as coisas q aprenddemos nas aulas anteiroes
for com listas


exemplo


0 Maria
1 Helena
2 Luiz

os indices sempre vão de 0 pra cima
"""

lista = ["Maria", "Helena", "Luiz", "Jooj", "Pe", "Juuj", "Isa"]
   
i = 0
for nome in lista:
    print(i, nome)
    i += 1


# ele fez usando i = range(len(lista))

# poderia ter feito tb for indice in i: print(i, lista[i])