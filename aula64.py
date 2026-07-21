"""
GERADOR CPFS
aula65 no notebook eu ahco?
"""

# existem varias formas de gerar numeros, por exemplo import random
import random

# ele tb meteu for _ in range(100): para executar o código inteiro 100 vezes e gerar 100 cpfs
nove_digitos = ""
rdigit = 0
for m in range(9):
    rdigit = random.randint(0, 9)
    nove_digitos += str(rdigit)

cpf = nove_digitos
cpfcomp = ""
soma1 = 0
multi1 = 0
i = 0
j = 10
while i < 9: # for digito1 in nove_digitos:
    pivot1 = int(str(cpf)[i]) #  resultado += int(digito1) * contador_regressivo; contador_regressivo -=1
    # print(pivot1)
    multi1 = pivot1 * j
    soma1 = soma1 + multi1
    i += 1
    j -= 1
    cpfcomp += str(pivot1)
# print(soma1)
resto1 = (soma1 * 10) % 11
digito1 = 0 if resto1 > 9 else resto1
# print("cpf comp: ",cpfcomp)
soma2 = 0
k = 0
l = 11
cpfstr = str(cpf) + str(digito1)
while k < 10:
    pivot2 = int(cpfstr[k])
    multi2 = pivot2 * l
    soma2 = soma2 + multi2
    k += 1
    l -= 1
resto2 = (soma2 * 10) % 11
digito2 = 0 if resto2 > 9 else resto2
# print(cpf)
cpfcomp = cpfcomp+str(digito1)+str(digito2)
# novocpf = cpf # enviado pelo usuario
print("cpf gerado:", cpfcomp)