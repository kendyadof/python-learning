# # variaveris livres + nonlocal (locals, global)
# print(globals()) # imprimir as variaveis globais
# def fora(x):
#     a = x # a é uma variável livre, q nao está definida dentro do escopo de "dentro"
#     def dentro():
#         # imprimir as variaveis locais
#         # print(locals())
#         print(dentro.__code__.co_freevars) # dentro tb é uma variável livre dentro do escopo dela mesma aqui
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1()) # a execução só ocorre aqui, quando coloca o parenteses junto de dentro1
# print(dentro2()) 

def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar=""):
        nonlocal valor_final
        valor_final += valor_a_concatenar # sem o nonlocal valor_final dá erro pois nao se pode ALTERAR o valor dessa variavel q está definida fora
        return valor_final
    return interna

c = concatenar("a")
print(c("b"))
print(c("c"))
print(c("d"))
final = c()
print(final)