# __new__ e __init__ em classes Python
# similar a construtores de outras linguagens
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls (e não o self).
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

class A(object):
    def __new__(cls, *args, **kwargs):
        # print("jooj antes do new")
        instancia = super().__new__(cls) # criação da instância
        # print("jooj depois do new")
        # instancia.x = 123
        return instancia

    def __init__(self, x):
        self.x = x
        print("init", self)
    
    def __repr__(self):
        return f"A()"
    
# a = A()
a = A(123)
# a = object.__new__(A)
# a.__init__()
# print(a)
print(a.x)