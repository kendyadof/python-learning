"""
argumentos nomeados e nao nomeados
nomeado tem sinalo de igual
nao nomeado recebe apenas o argmento (valor)"""

# def soma(x,y): # parametros
#     #print(x+y)
#     print(f'{x=} y={y}', "|", "x+y = " , x + y)

# print(soma)
# print(soma(1,2))
# soma(1,2) # argumento posicional (depende da ordem)
# soma(y=2,x=1) # isso "sobrepõe", isso sao argumentos nomeados

# agora com um Z

def soma(x,y,z): # parametros
    #print(x+y)
    print(f'{x=} y={y} z={z}', "|", "x+y+z = " , x + y + z)

# print(soma)
# print(soma(1,2))
soma(1,2,3) # argumento posicional (depende da ordem)
# soma(y=2,z=3, x=1) # isso "sobrepõe", isso sao argumentos nomeados
soma(1,2,z=5)
soma(1,y=2,z=5) # a partir do momento q vc passou um argumento nomeado, TODOS OS SEGUINTES DPS DELE terão q ser nomeados tb
print(1,2,3, sep="-")