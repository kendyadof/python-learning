# ele definiu essa aula como aula145.py, pq foi uma aula póstuma, adicionando no final da seção intermediária.
# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve
# ser !APENAS! posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# Keyword-Only Arguments (*) - * sozinho !NÃO SUGA! valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
# def soma(a,b,/,x,y): # barra: explicação na linha 16
#     print(a+b+x+y)

# soma(1, 2,3,y=3)
# suponhetamos que queira bloquear argumentos nomeados (pessoa botar x= ao inves de a)
# soma(x=1, y=2)
# Usa-se barra
# o q antes da barra nao pode ser nomeado na chamada, oq vem depois da barra pode ser livre: posicional ou nomeado.

#Keyword only arguments:
def soma(a,b,*args):
    print(args)
    print(*args) # eu fui testar pra lembrar desempacotamento
    print(a+b)

# suponhetamos q nao queira permitir args sugar todos os args.
# 8 = aqui acaba argumentos posicionais. Somente a e b são posicionais
def soma(a,b,*,c):
    print(a+b+c)

soma(1, 2, c=3) # isso nao impede colocar argumento nomeado no a e no b

def soma(a,b,/,*,c): # combinando os dois, nenhum argumento antes da barra deve ser nomeado, e dps do asterisco devem ser nomeados
    print(a+b+c)

soma(1, 2, c=3)

# E no fim, metendo um kwargs no final:
def soma(a,b,/,*,c, **kwargs): # combinando os dois, nenhum argumento antes da barra deve ser nomeado, e dps do asterisco devem ser nomeados
    print(kwargs)
    print(a+b+c)

soma(1, 2, c=3, nome="teste")