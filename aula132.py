# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
class Caneta:
    def __init__(self, cor):
        # self.cor_tinta = cor
        # self._cor = self.cor_tinta # "_cor nao deve ser usado"
        # private protected
        self.cor = cor
        self._cor_tampa = None
        # caso chame self.cor, ele ja chama o setter durante o init
        # self.cor = cor
        
    @property
    def cor(self):
        # print("PROPERTY")
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        # print("ESTOU NO SETTER",valor)
        if valor == "Rosa":
            raise ValueError("Não aceito essa cor")
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self,valor):    
        self._cor_tampa = valor


# def mostrar(caneta):
#     return caneta.cor

caneta = Caneta("Azul") # setter nao é executado quando está instanciando aqui
# caneta._cor
# caneta.cor = "Rosa"
caneta.cor = "Pink"
caneta.cor_tampa = "Azul"
# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)