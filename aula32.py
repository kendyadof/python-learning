"""
Faça um programa que peça ao usuário para digitar um numero inteiro, informe se este numero é par ou impar.
 Caso o usuario nao digite um numero inteiro, informe q não é um número inteiro
"""
numero = input("Digite um número inteiro: ")
numero_int = None
eh_par = None
# if not numero.isdigit: # eu esqueci de por  isdigit(), ESQUECI DO PARENTESES
try: # try except era a segunda solução
    numero_int = int(numero)
    eh_par = numero_int % 2 == 0
    if eh_par:
        print("O número é par") # ele usou variável pra guardar o texto do numero ser par tb, ja definindo o primeiro valor dela como "ímpar", dentro do if eh_par ele vira par
    else:
        print("O número é ímpar")
# else:
except:
    print("Esse número não é inteiro")
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
    Ex. Bom dia 0-11, Boa tarde 12-17, e Boa noite 18-23.
"""
# relogio=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
hora = int(input("Digite a hora: "))
# ele fez try except tb pra previnir a escrita de coisas q nao fossem inteiro

if hora <= 11: #  relogio[0:11]
    print("Bom dia!")
elif hora <= 17: #  relogio[12:17]:
    print("Boa tarde!")
else: # ele fez elif até 23, e acima de 23 era "Não conheço essa hora"
    print("Boa noite!")



"""
Faça um programa que peça o primeiro nome ao usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
    Se tiver entre 5 e 6, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
primeiro_nome = input("Digite seu primeiro nome: ")
tamanho = len(primeiro_nome)

if tamanho <= 4: # ele inventou de ser >= 1 por "a" não ser nome
    print("Seu nome é curto")
elif tamanho <= 6: #
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
