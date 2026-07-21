"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
# Loop infinito -> Quando um código não temm fim
"""
condicao = True
while condicao: 
    # print("dedo") # vai repetir enquanto a condição for verdadeira
    nome = input("Qual o seu nome? ")
    print(f'Seu nome é {nome}')
    if nome =="sair":
        break # dentro do while vc pode colocar break, ele procura o while mais próximo dele.
# print(123) # python pode comentar q o code is unreachable
# é muito bom usar debugger com while
print("Acabou é tetra")