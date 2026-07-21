# Exercício - Adia_somando execução de funções

# começa funcao nova
# def adia_soma(funcao):
#     yield funcao(5)
# termina funcao nova

# começa funcao nova
# def adia_multi():
#     yield multiplica(10)
# termina funcao nova

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


# ajudado por duck. ai
def criar_funcao(funcao, *pre_args):
    def adia(*post_args):
        return funcao(*pre_args, *post_args)
    return adia
    # if funcao == multiplica:
    #     return (funcao(*args)) * f1 * 2
# luiz otavio fez com x e y mesmo: *pre_args = x. *post_args = y
# EU NAO ENTENDI como q o programa nao dá problema quando ele nao sabe o y dentro do adia(y), ele simplesmente sabe
# s1 = adia_soma()
# for s in s1:
#     print(s)
# m1 = adia_soma(multiplica(10))
soma_com_cinco = criar_funcao(soma, 5)
# ele quer q o numero seja somado com 5 sempre
multiplica_por_dez = criar_funcao(multiplica, 10)

# ele quer q o numero seja multi por 10 sempre

# "essa função executa() está se precipitando"
# usa yield será?
# nao é com yield
# é com closure mesmo