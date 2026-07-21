"""
Calculadora com while
somente pedir dois numeros para o usuário, e um operador
operador pode só ser adição, subtração, divisão ou multiplicação
"""
sair = False
# fazendo com while True, ele fez um continue fora do except no final se fosse  um numero invalido
# para q fosse para o próximo loop do mesmo while
while not sair :
    try:
        num_1 = int(input("Digite o primeiro número: "))
        num_2 = int(input("Digite o segundo número: "))
        
        # ele tb fez um num_1_float, e o 2, pro caso de float
        # ele tb criou uma variavel chamada numeros_validos = None.
        # no true virou True, e no except continua None
        operador = input("Digite a operação (símbolo, + ou - ou * ou /: ")
        # ele tb fez q fosse possivel digitar mais de um operador, mas no caso, botar len(operador)>1, ent ta errado
        result = 0
        if operador == "+":
            result = num_1 + num_2 # ele tb fez f strings pra mostrar nas operações
            print("Resultado: ",result)
        elif operador == "-":
            result = num_1 - num_2
            print("Resultado: ",result)
        elif operador == "/":
            if num_2 == 0:
                print("Impossível dividir por zero.")
            else:
                result = num_1 / num_2
                print("Resultado: ",result)
        elif operador == "*":
            result = num_1 * num_2
            print("Resultado: ",result)
        else:
            print("Operador inválido!")
    except: # pode colocar tipo Exception como argumento. Assim: except Exception as error: print(error)
        # usar except sem nada é uma má prática, mas por enquanto tá ok
        print("Caractere inválido!")    
    # sair = input("Quer sair? ")
    # sair = sair.lower() # poderia usar .startsWith() tb, ou .endsWith(), jUNTO com o lower hehe
    sair = input("Quer [s]air? Digite qualquer outro caractere para continuar. ").lower().startswith("s")
    
    
