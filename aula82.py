def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# funcao = lambda parametro: parametro # má prática



print(
    executa(
        lambda x, y: x + y,
        2, 3
        # é tipo def lambda(x,y): . Mas lambda é uma "função anônima"! etb nao tem o "return!"
    )
    # seria a mesma coisa q passar:
    # executa(soma, 2, 3),
    # soma(2,3)
)


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m, 2
)

print(duplica(2))
# lambda GERALMENTE é pra coisa rápida e fácil. Se começar a ficar complicado, é pq tem algo errado com seu código

# tb pode-se usar args com lambda:
print(
    executa(
        lambda *args: sum(args), 1,2,3,4,5,6,7 # retorna 28
    )
)