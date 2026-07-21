"""
Execício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade:
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios"
"""
nome = input("Digite teu nome: ")
idade = input("Digite tua idade: ")
if nome != "" and idade != "": # ele fez if nome and idade, ou seja, se os dois forem true, já funciona. Se não, se ficar nulo, ficam false
    print(f"Seu nome é {nome}")
    print("Seu nome invertido é ",nome[::-1]) # pode fazer todas f strings tb
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print("A primeira letra do seu nome é ", nome[0])
    print("A última letra do seu nome é ", nome[len(nome)-1]) # ele fez nome[-1] como última letra
else:
    print("Desculpe, você deixou campos vazios")
