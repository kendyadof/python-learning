nome = 'João Pedro'
altura = 1.70
peso = 65
imc = peso / altura ** 2
# f-strings , formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura' # bota um f na frente e fecha o nome da variável com chaves. pra mostrar casas decimais, bota :. "numero de casas" f
print(linha_1)
linha_2 = f'pesa {peso} quilos e seu IMC é'
print(linha_2)
linha_3 = f'{imc:.2f}'
print(linha_3)
# print(nome, 'tem' , altura , 'de altura, pesa' , peso, 'quilos e seu IMC é',imc) # O PRINT JÁ PÕE ESPAÇO