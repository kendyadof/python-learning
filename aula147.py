# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# (cada coisa q vc faz com objeto usa um dunder method)
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y
                #  , z = "String"
                 ):
        self.x = x
        self.y = y
        # self.z = z
    
    # def __str__(self): # se quiser uma string desse objeto # ele faz um fallback pro repr caso str nao exista
    #     return f"({self.x}, {self.y})"

    def __repr__(self): # mais para desenvolvedor, como objeto é representado
        class_name = self.__class__.__name__ # ou type(self)
        # return f"{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})" # mostrar a repr de cada um, Z aparece com aspas
        return f"{class_name}(x={self.x!r}, y={self.y!r})"

    def __add__(self, other): # a adição de objeto ponto
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other): # a adição de objeto ponto
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        novo_y = self.y + other.y
        return resultado_self > resultado_other

# p1 = Ponto(1,2)
# p2 = Ponto(5,4)
# print(p1)
# print(repr(p2))
# print(f"{p2!r}") # exclamação pra escolher ou str ou repr

if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2?', p1 > p2)
    print('P2 é maior que p1?', p2 > p1)