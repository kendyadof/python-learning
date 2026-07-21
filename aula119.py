# lsita de tarefas (strings)
# mas com possibildade de desfazer e refazer ações
# input pro usuario digitar
# ele digita tarefas ou comandos
# comandos: listar, desfazer, refazer
# Rubber Ducking ou Rubber Duck Debugging = explicar o código pra alguém, ou um pato de borracha kk

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# checar se é comando, certo?
# listar = mosrtar tudo
# refazer (tentar refazer nada diz Nada a refazer)
# mesma coisa com Desfazer
# nao precisa agora mais ele colocou um clear na tela só.
# fazer cafe
# tomar banho
# a cada comando, ele lsita de novo (inclusive desfazer e refazer)

# nao tem problema desfazer, incluir nova, e refazer, colocando o desfeito no final. 

# luiz otavio fez um def listar(), e tb def desfazer() , def refazer() e def adicionar
# meu código ficou muito longe da margem, eu deveria modularizar no meu caso
desfazer = []
# refazer = [] # nao precisava mesmo
lista = []
ultimo = ""

# Aula seguinte: fazer o if null no def é um guard clause

while True:
    entrada = input("Comandos: listar, desfazer, refazer\nDigite uma tarefa ou comando: ")
    if entrada in ("desfazer","refazer","listar"):
        # print("Digitado comando:",entrada)
        if entrada == "desfazer":
            if not lista:
                print("Nada a desfazer")
                continue
            else:
                ultimo = lista.pop(-1) # -1 nao precisava
                desfazer.append(ultimo)
                print("LISTA DE COMPRAS:") 
                for item in lista:
                    print(item)
                # print("   PARA DEBUG   , DESFAZER:")
                # for item in desfazer:
                #     print(item)
                # print("   FIM DEBUG DESFAZER   :")
        elif entrada == "refazer":
            if not desfazer:
                print("Nada a refazer")
                continue
            else:
                ultimo = desfazer.pop(-1)
                lista.append(ultimo)
                print("LISTA DE COMPRAS:") 
                for item in lista:
                    print(item)
                # print("   PARA DEBUG   , REFAZER:")
                # for item in refazer:
                #     print(item)
                # print("   FIM DEBUG REFAZER   :")
        else: # listar
            if not lista:
                print("Nada a listar")
                continue
            else:
                print("LISTA DE COMPRAS:") 
                for item in lista:
                    print(item)
    else: # items, tarefas
        lista.append(entrada)
        # refazer.append(entrada)
        # desfazer.append(entrada)
        for item in lista:
            print(item)
    print("#" * 10)

# do luiz:
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue

# explicação de guard clause:
while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        "listar": lambda: listar(tarefas), # lambda para adiar a função,ao inves de executar na declaração do dict
        "desfazer": lambda: desfazer(tarefas, tarefas_refazer),
        "refazer": lambda: refazer(tarefas, tarefas_refazer),
        "clear": lambda: os.system('clear'),
        "adicionar": lambda: adicionar(tarefa, tarefas)
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos["adicionar"] # o adicionar era um else
    comando()