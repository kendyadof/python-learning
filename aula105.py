# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): # é a fabrica de decoradores q vai configurar um decorador
    def fabrica_de_funcoes(func): # é o decorador q recebe uma função
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # é a sua funcao (tipo soma)
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

# ANOTACAO MINHA SEM PRINT PRA ENTENDER MELHOR:
def fabrica_de_decoradores(a=None, b=None, c=None): # é a fabrica de decoradores q vai configurar um decorador
    def fabrica_de_funcoes(func): # é o decorador q recebe uma função
        def aninhada(*args, **kwargs): # é a sua funcao (tipo soma)
            return func(*args, **kwargs)
        return aninhada
    return fabrica_de_funcoes
# FIM ANOTACAO


@fabrica_de_decoradores(1, 2, 3) # isso de @decoradora tb executa a função decoradora. # ao botar parenteses (), tb executa (antes do python)
def soma(x, y): # essa funçao no padrã\o tb é enviada como argumento
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)