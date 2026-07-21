"""
COMO RESOLVER ALGUNS PROBLEMAS, USANDO REPLACE() POR EXEMPLO

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma1 dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO1,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO1
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto1 da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re # regular expression
# import sys # luiz otavio q colocou

entrada = input("CPF: ")
cpffull = re.sub(
    r"[^0-9]", # substitui tudo q nao é um numero
    "",
    entrada
    ) # tb substitui
# cpffull = "746.824.890-70" \
#     .replace(".","") \
#     .replace(" ","") \
#     .replace("-","") 
nove = cpffull[:9]
e = 0
f = 0
rep = ""
flag = False
while f < 10:
    while e < 11:
        rep+=str(f)
        e+=1
    # print("rep: ", rep)
    if entrada == rep:
        flag = True
    rep = ""
    e = 0
    f+=1

# # como o luiz otavio fez: ele repete oprimeiro caractere pelo tamanho len() da entrada
# entrada_e_sequencial = entrada == entrada[0] * len(entrada)
# if entrada_e_sequencial:
#     print("Você enviou dados sequenciais.")
#     sys.exit() # metodo luiz otavio

cpf = cpffull # ele fez "74682489070". nove_digitos = cpf[:9]
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
while k < 10:
    pivot2 = int(str(cpf)[k])
    multi2 = pivot2 * l
    soma2 = soma2 + multi2
    k += 1
    l -= 1
resto2 = (soma2 * 10) % 11
digito2 = 0 if resto2 > 9 else resto2
# print(cpf)
cpfcomp = cpfcomp+str(digito1)+str(digito2)
# novocpf = cpf # enviado pelo usuario
if flag == False:
    if cpfcomp == cpf:
        print("Válido")
    else:
        print("CPF inválido")
else:
    print("CPF inválido")

