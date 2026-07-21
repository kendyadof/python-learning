# classes decoradoras (decorator classes)

class Multiplicar:
    def __init__(self,  multiplicador):
        # print("INIT", func)
        # self.func = func
        self._multiplicador = multiplicador

    # def __call__(self, *args, **kwds):
    #     # print(args, kwds)
    #     resultado = self.func(*args, **kwds)

    #     return resultado * self._z

    def __call__(self, func):
        def interna(*args, **kwds):
            resultado = func(*args, **kwds) # adiando a execução
            return resultado * self._multiplicador
        return interna

# @Multiplicar # letra maisucula pq é classe
@Multiplicar(10) # tb funciona com parenteses, mas o comportamento é diferente, aí ele tá chamando o init() do multiplicar
def soma(x, y):
    return x + y

dois_mais_dois = soma(2,2)
print(dois_mais_dois)