# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None # primeiro configura a property
        self.name = name

    @property # a property é desta classe aqui
    # @abstractmethod
    def name(self): 
        return self._name
        # return self._name
        # return self._name

    @name.setter # tem q mover o seter pra baixo tb
    @abstractmethod
    def name(self, name): ... 
        # return self._name


class Foo(AbstractFoo):
    # name = "" # criando isso ao inves da property, tb funciona
    # relembrando: property é um método q se comporta como atributo.
    # se colocar um atributo, ent funciona
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    # @property # a property é desta classe aqui. O de cima forçou a criar a property aqui
    # def name(self):
    #     return self._name
    #     # return self._name

    # @name.setter  # name is not defined
    # def name(self, name): 
    #     self._name = name

    @AbstractFoo.name.setter # assim q ele pega o name (property) da super
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)