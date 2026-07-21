# operadores logicos
# (relembrando)
# and, or, not
# and todas sao verdadeiras, exceto quando a outra for falsa, aí o and é falso
# Tb existe o None, pra representar um não-valor
# 0    0.0    ''   e False são todos False
# essa segunda aula fala só do or

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = 'senha'
# if (entrada == 'E' or entrada=='e') and senha_digitada==senha_permitida: # oq está em parênteses será avaliado primeiro
#     print('Entrar')
# else:
#     print('Sair')

# 
# 
# 
# 
# 
# 
# 
# avaliacao de curto circuito de or
print(True or False or 0 ) # = True
print(False or False or 0 or 'abc' ) # = True por causa do abc

senha=input("Senha: ") or 'Sem senha'
print(senha)  # digitar nada vai retornar Sem senha texto