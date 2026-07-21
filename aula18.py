# debug no vscode, depuração
# tem um botãozinho de play com um bug
# ELE CHAMOU O LAUNCH.JSON DE LUNCH FILE
# precisa informar o debugger e o interpretador onde vc quer q o interpretador  vai parar
# clicar na linha pra ter uma bolinha vermelha, isso vai ser chamado de break point
# ao debugar, e ao parar no break point, vao ter alguns controles pra mexer, de avançar, voltar, refazer, parar, etc
# usará bastante o step over 
condicao = False # condicao = True, seria a mesma coisa q condicao = 10 == 10 
condicao2 = True
if condicao:
    print("código do primeiro if")
elif condicao == False:
    pass # vc pode escrever pass para nao fazer nada
elif condicao2 :
    pass # se a primeira condição for satisfeita, ele nao vai executar o resto do elif/else
else:
    print("código do primeiro else")

if 10 == 10:
    print("Outro if")

print("Fora do bloco do if")


# ele tb fez outro review explicando melhor if elif e else