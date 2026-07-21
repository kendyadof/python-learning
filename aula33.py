"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis q vimos:  str, int, float, bool
built-in = embutidos (no python)
"""
string = "luiz Otávio" # esse valor é imutável
# outra_variavel = string
outra_variavel = f'{string[:3]}ABC{string[4:]}' # pegando entre 0 ao 3 - gerando uma nova variável, e do 4 ao final
# string[3] = "" # isso não é possível, pq é imutável
# a primeira variável continua a mesma coisa pq é imutável
# print(string)
print(outra_variavel)
print(string.capitalize()) # capitalizar por exemplo
print(string) # após digitar ponto (.) olhar a setinha no canto dirteito,q  vai abrir um menu explicando cada comando
print(string.zfill(100)) # ele põe 100 zeros à esquerda da string até completar tantos caracteres na string total

# ler a documentação é uma boa prática de programação
