# Exercício - sistema de perguntas e respostas

# a pessoa vai escolher a resposta conforme o número de índice da lista (chave) e não o valor literalmente

#pode contar se quiser, quantas a pessoa acertou
# pode-se incluir quantas perguntas quiser no dict, dinamicamente, q ele vai perguntar todas!!
# exemplo de texto final: vocce acertou x de 3 perguntas

# caso digite qualquerr coisa ao inves dos indices, tb considerar erro

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# ISSO É UMA LISTA DE DICIONÁRIOS!

ichave = 0
ivalue = 0
# itupla = 0
ipergunta = 0
iacertos = 0

# perguntas[dict1{v1,v2},dict2{},dict3{}]
# acesso a cada dict:

while ipergunta < len(perguntas):
    pergunta = perguntas[ipergunta]
    # print("Segunda pergunta: ",perguntas[1])
    # pergunta é dict1
    # for chave in pergunta.keys():
    
    while ichave < len(pergunta.keys())-1:
        while ivalue < len(pergunta.values())-1:
        # while ivalue < len(pergunta.values())-1:
            print(
                list(pergunta.items())[ichave][ivalue]
            )
            ivalue += 1
        ichave += 1
        ivalue = 0
    opcao = input("Digite o INDEX da resposta VALUE q vc acha: ")
    intopcao = int(opcao)
    # dentro de um list(dict.keys())[index], key tb é index

    # para comparar opção digitada com opção certa:
    valoropcao = list(pergunta.get("Opções"))[intopcao]
    intvaloropcao = int(valoropcao)
    resposta = (pergunta["Resposta"])
    intresposta = int(resposta)

    if intvaloropcao == intresposta:
        print("Acertou mizerávi!!!")
        iacertos += 1
    else:
        print("Fala holandês! Qual a resposta?! ... ERRÔ!!!!")
    # fim comparação
    ichave = 0
    # itupla += 1
    ipergunta+=1
        # if ipergunta == 3:
        #     break
    # itupla = 0
    ivalue = 0
    
print("Perguntas acertadas: ", iacertos)

# SOLUCAO
# NEM PRECISAVA por .keys .items.
# exemplo:
# pergunta["Pergunta"]
# pergunta["Opções"]
# ele tb usou fors, nao whiles
# ele, pra printar com indices nas op~çoes:
# for i, opcao in enumerate(pergunta["Opções"]):
#      print(f"{i})", opcao)



# -------------------------------------------------------------------------------------------
# # Exercício - sistema de perguntas e respostas


# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')
# ----------------------------------------------------------------------------------------------------------
# MINHAS TENTATIVAS:
# for pergunta in perguntas:
#     # pergunta é dict1
#     # for chave in pergunta.keys():
#     while ichave < 2:
#         while ivalue < len(pergunta.keys())-1:
#             print(
#                 list(pergunta.items())[ichave][ivalue]
#             )
#             ivalue += 1
#         ichave += 1
#     ivalue = 0
#     ichave = 0


# while k < len(perguntas):
#     pergunta = list(perguntas)[k]
#     lista_chaves = list(pergunta.keys())
#     lista_valores = list(pergunta.values())
#     lista_items = list(pergunta.items())
#     while j <  len(list(pergunta.keys())):
#         while i < 2:
#             # lista = list(pergunta.values())
#             valor = lista_items[i]
#             print(valor)
#             i += 1
#         # valor = pergunta[chave]
#         # print("V: ",valor)
#         i = 0
#         j += 1
#     # print("V: ",pergunta)


# for pergunta in perguntas:
# while k < len(perguntas):
#     pergunta = list(perguntas)[k]
#     lista_chaves = list(pergunta.keys())
#     lista_valores = list(pergunta.values())
#     lista_items = list(pergunta.items())
#     while j <  len(list(pergunta.keys())):
#         while i < 2:
#             # lista = list(pergunta.values())
#             valor = lista_items[i]
#             print(valor)
#             i += 1
#         # valor = pergunta[chave]
#         # print("V: ",valor)
#         i = 0
#         j += 1
#     # print("V: ",pergunta)
    
    





# dici = dict(perguntas)
# print(list(dici.values()))

# pergunta = pergunta em si, chave e valor
# i = contador q NAO considera a chave resposta dentro de pergunta
# i = 0
# for pergunta in perguntas:
#     while i < 2:
#         print(pergunta.items(i))
#         i += 1
#     # print(chave, valor)
#     opcao = input("Escolha uma opção: ")
#     listaopcao = list (pergunta.values())
    
#     if perguntas.values("Opções")[opcao] == perguntas.values("Resposta"):
#         print("Acertou mizerávi!!!")
#     else:
#         print("Fala holandês! Qual a resposta?! ... ERRÔ!!!!")