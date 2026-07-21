"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""
# escopo do módulo: do arquivo .py
x = 1


def escopo():
    # global x
    x = 10 # se comentar esse x, ele busca o x mais proximo do escopo para definir.

    def outra_funcao(): 
        # global x
        x = 11 # se comentar esse x, ele busca o x mais proximo do escopo para definir. De dentro pra fora, fora pra dentro nao existe
        y = 2
        print(x, y)

    # num debugger, ele vai do def outra_funcao() pra cá direto
    outra_funcao()
    print(x)
    # print(y) # sem acesso

# num debugger, ele vai do def escopo() pra cá direto
print(x)
escopo()
print(x)

# call stack = ppilha de chamadas