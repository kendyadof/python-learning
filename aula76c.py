# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy #explicado em linha 89

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'sobrenome': 'Miranda 2', # ao colocar chaves duplicadas, ok, mas somente o último valor será considerado para a chave.
    # 'sobrenome': 'Miranda 3', # 
    # 'idade': 900, # PODE-SE DEIXAR UMA VÍRGULA NO FINAL PRA CASO QUEIRA ADD MAIS COISA
}

# métodos com dois underlines (__) são dunder/dander??? dunder lion. Enfim, são métodos importantes.
# print(pessoa.__len__())
# print(len(pessoa)) # 3

# print(pessoa.keys()) # dict_keys(['nome', 'sobrenome', 'idade'])
# pra pegar as chaves
# # é possível fazer coerção de dados com isso
# print(tuple(pessoa.keys())) # ('nome', 'sobrenome', 'idade')
# print(list(pessoa.keys())) # ['nome', 'sobrenome', 'idade']
# for chave in pessoa: # ou pessoa.keys()
#     print(chave)

# print(list(pessoa.values()))
# pra pegar os valores das chaves
# for valor in pessoa.values():
#     print(valor)


# tb tem por items, ITEMS!!!!!!
# sendo chaves  E VALOR
# print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave, valor)


# # É possível setar um valor padrão para o get. Deixando a chave "idade" comentada no dict (pra ela não existir)
# pessoa.setdefault("idade", None) # colocando como none pq SE a chave não existir, ele seta um valor padrão e não dá exception
# # caso EXISTA, o setdefault() não fará nada
# print(pessoa["idade"]) 

# SEGUNDA AULA, a partir de copy()

# a lista tem um método copy(), e o dict do python tb tem método copy() (sendo ambos mutáveis)
# shallow copy significa cópia rasa


# d1 = {
#     'c1': 1,
#     'c2': 2, # PODE-SE DEIXAR UMA VÍRGULA NO FINAL PRA CASO QUEIRA ADD MAIS COISA

# }

# # d2 = d1 # aqui, não está copiando os valores aqui para d2, ele simplesmente diz q d2 aponta para o mesmo dict q d1

# # d2["c1"] = 1000
# # print(d1) # d1 tb será afetado pela atribuição acima  


# d2 = d1.copy()

# # d2["c1"] = 1000
# # print(d1) # assim, d1 não afeta d2 (ainda é cópia rasa, copia tudo q é imutável)

# d1 = {
#     'c1': 1,
#     'c2': 2, 
#     "l1": [0,1,2], # PODE-SE DEIXAR UMA VÍRGULA NO FINAL PRA CASO QUEIRA ADD MAIS COISA
#     # lista é mutável
# }

# d2 = d1.copy() # no caos da lista (q é imutável) ele nao vai copiar, e sim fazer d1 e d2 apontarem pra mesma lista na memória
# # cópia rasa = ele nao entra em sub-níveis
# d2["c1"] = 1000
# d2["l1"][1] = 999999
# print(d1) # ambos os dict apontam pra mesma lista em tal índice

# agora, CASO queira copiar tudo mesmo, o python tem um módulo de copy 
# explicação do import la em cima.
# deepcopy é cópia profunda
# d2 = copy.copy(d1) # cópia rasa
# d2 = copy.deepcopy(d1) # cópia profunda
# # pra tudo q for mutável
# d2["c1"] = 1000
# d2["l1"][1] = 999999

# print(d1)
# print(d2)

# TERCEIRA AULA DE MÉTODOS ÚTEIS DE DICT

p1 = {
    "nome": "Luiz",
    "sobrenome" : "Miranda"
}
# print(p1["nome"])
# print(p1.get("nome", "Não existe")) # caso o nome nao eixste, esteja comentado no dict, o get nao retorna exception, e sim "Não existe"

# nome = p1.pop("nome") # retorna o valor da chave, mas tb remove ela
# print(nome)
# print(p1)

# o popitem apaga o ULTIMO adicionado
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# atualizar o dict (por chaves): # se passar completamente vazio, ele nao faz nada, o dict fica do mesmo jeito q tava antes
# exemplo: p1.update({})
# p1.update({
#     "nome" : "novo valor",
#     "idade" : 30, # neste caso, nova chave, usando o update() 
# })

# agora, passando via argumentos nomeados:
# p1.update(nome="novo valor", idade=30)


#terceira forma: com tupla ou lista

# tupla = (("nome", "novo valor"), ("idade", 30))
# p1.update(tupla)

# lista = [["nome", "novo valor"], ["idade", 30]]
# p1.update(lista)

# enfim, update() pode receber um ITERÁVEL


print(p1)