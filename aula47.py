"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, vc vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra
    - Se a letra digitada n ão estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
# contador = 0
# secreta = "elotrolado"
# tentativa_str = ""
# tentativa = list("**********")
# j = 0
# while True:

#     letra = input("Digite uma letra: ")

#     if len(letra) > 1:
#         print("Digite apenas uma letra")
#         continue
#     else:
#         for i in secreta:
#             if letra == i:
#                 tentativa[j] = letra
#             j += 1
                
#         if "*" not in tentativa:
#             print("VOCÊ GANHOU, PARABÉNS!")
#             print("A palavra era: ", secreta)
#             print("Tentativas: ", contador)     
#             tentativa = list("**********")
#             tentativa_str = ""
#             contador = 0
#             j = 0
#             continue
        
#         # if len(tentativa_atual) == len(secreta):
#         #     for j in tentativa_atual:
#         #         if j == "*":
                    
#         #     tentativa = tentativa_atual
#         #     tentativa_atual = ""
#         tentativa_str = "".join(tentativa)
#         print("Palavra formatada: ", tentativa_str) 
#         contador += 1 
#         j = 0
        # exemplo sendo palavra secrta = perfume
        # ***** = a letra digitada não existe na palavra
        # se digitar letra e:
        # print("*e****e") # = pErfumE
        # se continuar dando enter sem introduzir nada, vai continuar mostrando *e****e *e****e *e****e *e****e
        # contando tentativas
                # quando terminar = advininhar todas as letras
                # print("VOCÊ GANHOU, PARABÉNS!")
                # print("A palavra era: perfume")
                # print("Tentativas: 24 = CONTADOR DE TENTATIVAS")
                # print("digite uma letra") # ELE REINICIA E COMEÇA O JOGO DE NOVO





# enfim, na solução  o luiz otavio fez:
# letras_acertadas = "" # string
# palavra_secreta = "perfume"
# numero_tentativas = 0
# while True:
#   letra_digitada = input("digite uma letra: ")
#   numero_tentativas += 1
#   if len(letra_digitada) > 1 : 
#       print("Digite apenas uma letra")
#       continue
#   # ele nao fez else npo if, só fez continue
#   if letra_digitada in palavra_secreta:
#       letras_acertadas += letra_digitada # ele está salvando só as letras acertadas
#   palavra_formada = ""
#   for letra_secreta in palavra_secreta:
#       if letra_secreta in letras_acertadas:
#           palavra_formada += letra_secreta
#       else:
#           palavra_formada += "*"
#   # a palavra formada FORMA  a palavra secreta
#   print("Palavra formada: ", palavra_formada)
 
#   if palavra_formada == palavra_secreta:
#      #  aqui usa o   os.system("clear") explicado no final do código
#       print("Voce ganhou parabens")
#       print("A palavra era", palavra_secreta)
#       print("Tentativas: ")
# # 
# # ele usou outra string pra gravar letras acertadas, aí guarda as certas do usuario, pra dps colocar no if pra comparar palavras formadas
# 
# existe um modulo pra fazer o python dar clear na tela:
# la no começo do programa, digitgar:
# import os
# 
#   quando vc quiser colocar o clear:
#   os.system("clear")

# solução direto do github:
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        # os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0