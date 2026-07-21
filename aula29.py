"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
# print(1234)
# print(456) # isso o python ainda lê
# int('a') # ValueError é o nome do erro
# float('a') #  ValueError

numero_str = input("Vou dobrar o número que você digitar: ")
# print(numero_str.isdigit()) # usa tabela unicode, verifica se é apenas números. Ponto tb dá false
# if numero_str.isdigit(): # if não evita erros, vulgo exceções
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2}")
# else:
#     print("Isso não é um número")
# selecionar a variável, sublinhar inteira, e apertar F2, permite mudar o nome dela em todas as ocorrências

try:
    print("STR: ", numero_str)
    numero_float = float(numero_str)
    # ele vai pular o  trecho após o erro
    print("FLOAT: ", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")
except:
    print("Isso não é um número")

# é possível capturar o erro/exceção
# não é muito prudente usar try except assim, mas isso é só pra ser o básico