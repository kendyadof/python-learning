frase = "O python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum."
"""
pode usar \ pra quebrar linhas muito grandes fora das aspas
Enfim, exercício:
    Tem a frase.
    Qual a letra apareceu mais vezes nessa frase? 
    Usar while para contar

"""
# print(frase.count("Python")) # conta quantas vezes o argumento entrado apareceu na frase.
# pode usar .lower() tb, ou na frase ou na count().
# maiúsculo é .upper()
# lembrand q ã é diferente de a
# print(frase.count("o"))

# índice
i = 0

# pivô, marcando a maior até então
j = 0

# numero de ocorrencias na letra atual
contagem_atual = 0

# alfabeto
# alfabeto = "abcdefghijklmnopqrstuvwxyz"

# caracteres em ocorrencias
ocorrencias = ""

# contagem ocorrencias
cont_ocorrencias = ""

# letra atual
letra_atual = ""

# maior quantidade encontrada até o momento
maior_atual = ""
# ele printou na solução: cada vez do loop por uma letra  direto...dps tirou
while i < len(frase) :
    letra_atual = frase[i].lower()
    if letra_atual == " ":
        i += 1
        continue
    else:
        if letra_atual in ocorrencias:
            i+=1
            continue
        else:
            contagem_atual = frase.count(letra_atual)
            ocorrencias += letra_atual
            cont_ocorrencias += f"{letra_atual}: {contagem_atual} ocorrências. \n"
            if contagem_atual > j:
                j = contagem_atual
                # ocorrencia com j é a maior por enquanto
                maior_atual = frase[i]
            else:
                i += 1
                continue
                # maior_atual = frase[i]
            # contagem_str = str(contagem_atual)
            # ocorrencias += "letra ",letra_atual," : ",contagem_str,"\n"
        
    i += 1
print("A letra encontrada mais vezes foi: ",maior_atual,", com ",j," ocorrências")
print("Ocorrências diferentes: ", ocorrencias)
print("Contagem de cada uma detalhada: ")
print(cont_ocorrencias)