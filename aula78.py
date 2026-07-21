# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# é diferente de dicionario, q tem um par de valores
# # s1 = set('Luiz')
# s1 = set()  # vazio 
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 3, 1}  # com dados
# eles naturalmente eliminam valores duplicados

l1 = [1,2,3,3,3,3,3,1]
s3 = set(l1)
l2 = list(s3)
print(l2)

s2 = {1,2,3}
print(3 in s2)
# for funciona:
for numero in s2:
    print(numero)

# tupla pode, mas nao set nem dict dentro de outro set (valores mutáveis nao podem ser usados em set)
# mas sets nao garantem ordem


# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add("Olá")
s1.add(1)
# s1.update("Olá mundo")
# ou ainda, mande um iteravel em si:
s1.update(("Olá mundo",1,2,3,4))
# clear() limpa o set niteiro
# s1.clear()
# discard() descarta valores
s1.discard("Olá mundo")
s1.discard("Olá")
print(s1)
s1.clear()
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda (a ordem importa)
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s2 ^ s1 # nesse caso a ordem nao importa
print(s7)