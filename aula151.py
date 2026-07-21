# Funções decoradoras e decoradores com classes

def meu_repr(self): # usar o repr aqui ao inves de ter umem casa classe abaixo
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr

# tb funciona a meu_repr fora da adiciona_repr

def adiciona_repr(cls): # função decoradora
    # def meu_repr(self): # usar o repr aqui ao inves de ter umem casa classe abaixo
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f"{class_name}({class_dict})"
    #     return class_repr
    cls.__repr__ = meu_repr
    return cls # classe decorada

# class MyReprMixin:
#     def __repr__(self): # usar o repr aqui ao inves de ter umem casa classe abaixo
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f"{class_name}({class_dict})"
#         return class_repr

# class SuperTime:
#     ...
@adiciona_repr
class Time: # time de futebol
    def __init__(self, nome):
        self.nome = nome
@adiciona_repr
class Planeta: 
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

Planeta = adiciona_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)