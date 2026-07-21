# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        # private # protected # ou public
        # encapsulamento
        self.cor_tinta = cor

    @property
    def cor(self): # método se comportando como atributo
        print("PROPERTY")
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456

############################################
# código cliente:
caneta = Caneta("Azul")
print(caneta.cor)
print(caneta.cor_tampa) # se botar parenteses ele tenta ser callable.



# class Caneta:
#     def __init__(self, cor):
#         # private # protected # ou public
#         # encapsulamento
#         self.cor = cor

#     def get_cor(self): # getter
#         print("GET COR")
#         return self.cor 
# ############################################
# # código cliente:
# caneta = Caneta("Azul")
# print(caneta.get_cor())