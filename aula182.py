# secrets gera números aleatórios seguros (para criptografia por ex)
import secrets
import string as s # pra ensinar sobre senhas
from secrets import SystemRandom as Sr


print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
# comando direto no terminal:
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

# print(secrets.randbelow(100))
# print(secrets.choice([10,11,12]))
random = secrets.SystemRandom() # agora oq rodar no random vai ser aleatorio mesmo
# random.seed(0) # agora nao faz nada devido ao systemrandom()
r_range = random.randrange(10, 20, 2)
# print(r_range)

r_int = random.randint(10, 20)
# print(r_int)

r_uniform = random.uniform(10, 20)
# print(r_uniform)


nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)
# print(nomes)


novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# print(random.choice(nomes))

