# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        # retorno = super().upper()
        retorno = super(MinhaString, self).upper() # mesma coisa q a linha de cima
        print('DEPOIS DO UPPER')
        return retorno
        # return "ABC"
        # super() # chama o da super
        

# string = MinhaString('Luiz')
# print(string.upper())


class A:
    atributo_a = "valor a"

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")

class B(A):
    atributo_b = "valor b"

    def __init__(self, atributo, outra_coisa): # sobrepondo init e atributos
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("B")

class C(B):
    atributo_c = "valor c"

    def __init__(self, *args, **kwargs): # sobrepondo init e atributos
        # print("EI burlei o sistema")
        super().__init__(*args, **kwargs)
        

    def metodo(self):
        # super(C, self).metodo() # sendo explicito
        # super().metodo()
        # super(B, self).metodo() # sendo explicito # a partir de B, busca o super (vai ser o A)
        A.metodo(self) # o recomendavel é usar o de cima, com super() mesmo
        B.metodo(self)
        print("C")

# c = C()
c = C("atributo", "qualquer")
# print(c.atributo)
# print(c.outra_coisa)
# print(c.atributo_a)
c.metodo()
# print(C.mro())