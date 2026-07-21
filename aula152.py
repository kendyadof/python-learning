# Funções decoradoras e decoradores com métodos

def meu_repr(self): # usar o repr aqui ao inves de ter umem casa classe abaixo
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr

def adiciona_repr(cls): # função decoradora
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if "Terra" in resultado:
            return "Você está em casa"
        return resultado
    return interno

@adiciona_repr
class Time: # time de futebol
    def __init__(self, nome):
        self.nome = nome
@adiciona_repr
class Planeta: 
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f"o planeta é: {self.nome}"


brasil = Time('Brasil')
portugal = Time('Portugal')

Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())