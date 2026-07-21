"""
split e join com list e str
split - divide umma string - retornando uma lista
join - une uma string
"""
frase = "Olha só que, coisa interessante"
lista_palavras = frase.split() # ao usar com argumento vazio, o default (None) vai separar qualquer whitespace character e espaços
print(lista_palavras)

lista_frases = frase.split(",") # tb pode-se usar ", " (virgula e espaço, já q geralmente separamos frases assim)
lista_fixed = []
for i, frase in enumerate(lista_frases):
    # print(lista_frases[i].strip()) # tb tem lstrip() e rstrip(). strip() corta os espaços do início e do fim
    # lstrip() corta só o espaço da esquerda
    # rstrip() corta só o espaço da direita

    # lista_frases[i] = lista_frases[i].strip()
    # nao é muito legal alterar listas assim, mas é possível
    # enfim, fazser assim:
    lista_fixed.append(lista_frases[i].strip())
print(lista_frases) 

# agora quero unir novamente essas frases
# frases_unidas = "-".join("abc") # saída: a-b-c
frases_unidas = "-".join(lista_frases) # o caractere vai ser utilizado como separador dos itens da lista iteravelmente da frase
print(frases_unidas) # saída : Olha só que- coisa interessante