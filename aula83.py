# Empacotamento e desempacotamento de dicionários
a, b = 1, 2 # desempacotando
a, b = b, a # empacotamento (invertendo os valores)
# print(a, b)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}


# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1,b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# # é tipo fazer isto:
# # fazendo só valor
# for valor in pessoa.items():
#     print(valor)

# # fazendo chave e valor
# for chave, valor in pessoa.items():
#     print(chave, valor)
# print(b, type(b))
# args e kwargs:
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

# se quiser juntar dicionários:
dados_pessoa = {
    "idade": 16,
    "altura": 1.6
}

# colocar no terceiro dicionário a extração dos valores, extrair os valores
pessoas_completa = {**pessoa, **dados_pessoa} # vai pegar todos os elementos do primeiro dicionário
# pessoas_completa = {**pessoa, "chave": 1}
# isso foi o DESEMPACOTAMENTO de um dicionário na linha 42

# print(pessoas_completa)

# kwargs vao ser empacotados na função
def mostro_argumentos_nomeados(*args, **kwargs): # kwargs sempre vai usar dois asteriscos - aqui tá EMPACOTANDO or argumentos no kwargs
    print("não nomeados: ", args) # os NAO NOMEADOS na função serão o args de qualquer jeito, nao vao entrar no kwargs
    print("nomeados:")
    for chave, valor in kwargs.items():
        print(chave,valor)

# mostro_argumentos_nomeados(1, 2, nome="Joana", qlq=123)
# pode-se desempacotar para chamar a função:
# mostro_argumentos_nomeados(**pessoas_completa)
# desempacotando uma chamada de função


configuracoes={
    "arg1": 1,
    "arg2": 2,
    "arg3": 3,
    "arg4": 4,
}


mostro_argumentos_nomeados(**configuracoes)
# é pra isso q serve empacotamento e desempacotamento.