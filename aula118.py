# problema dos parametros mutáveis em funções python
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes("luiz") # ao nao passar argumento, o python nao vai executar o parametro lista[] de novo
# todas as vezes q chamar a função sem argumento, a mesma lista será usada na memória
# pois a lista é um parametro mutável. Qualquer mutável vai dar esse problema
# argumentos padrão, no caso
adiciona_clientes("Joana", cliente1)


cliente2 = adiciona_clientes("helena")
adiciona_clientes("maria", cliente2)
print(cliente1)
print(cliente2)

# resolvimento:
# lista1 = []
# cliente1 = adiciona_clientes("luiz",lista1)
# ou
# def adiciona_clientes(nome, lista=None):
    # if lista is None:
    #     lista = []
    # ...

# com None assim é melhor