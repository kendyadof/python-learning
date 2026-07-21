# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe) # bases: heranças em ordem
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# object acima
# class Foo:
#     ...

# Foo = type("Foo", (object,),{}) # {} é o dict da classe
# f = Foo()
# # print(isinstance(f,Foo))
# print(type(f))
# print(type(Foo))

def meu_repr(self):
    return f"{type(self).__name__} ({self.__dict__})"

# segunda aula:
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('MEU NEW METACLASS')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        # print(cls.__dict__)
        if "falar" not in cls.__dict__ or not callable(cls.__dict__["falar"]):
            raise NotImplementedError("implemente Falar")

        return cls
    
    def __call__(cls, *args, **kwds):
        instancia = super().__call__(*args, **kwds)
        # print(instancia.__dict__)

        if "nome" not in instancia.__dict__:
            raise NotImplementedError("crie o attr nome")

        return instancia

# class Pessoa(object, metaclass=type):
class Pessoa(metaclass=Meta):
    falar = 123 # isso faz o falar nao ser callable
    def __new__(cls, *args, **kwargs):
        print('MEU NEW WILL WILL WILL')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome): # inicializando os attr da instância
        print('MEU INIT')
        self.nome = nome
    
    def falar(self): #  faz falar ser callable
        print("falando")

p1 = Pessoa('Luiz')
# print(p1.attr)
# print(p1.falar())
p1.falar()
