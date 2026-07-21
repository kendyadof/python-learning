"""
Faça uma lista de compras com listas. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
opcao = ""
lista = list("") # lista = []
item = ""
indice = 0
removido = 0
while opcao != "s": # while True
    try:
        opcao = input(f"Selecione uma opção\n [i]nserir [a]pagar [l]istar (ou [s]air): ")
        if opcao == "i":
            # ele tb mandou os.system("clear") pra limpar a tela
            item = input("Digite o novo item para ser inserido: ")
            lista.append(item)
        elif opcao == "a":
            indice = int(input("Escolha o índice para apagar: "))
            try:
                removido = lista.pop(indice) # del lista[indice]
            except: # poderia ser except ValueError e depois except IndexError pra tratar separadamente
                print("Não foi possível apagar esse índice.")
        elif opcao == "l":
            if len(lista) == 0:
                print("Nada para listar. ")
            else:
                for index, produto in enumerate(lista):
                    print(index, produto)
        elif opcao == "s":
            print("Saindo...")
        else:
            print("Opção inválida")
    except: # ele nao usou try except por fora do apagar
        continue