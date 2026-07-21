# Exercício: exportar lista de tarefas para JSON
import os
import json

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

def exportar(tarefas):
    # luiz fez uma função para ler e outra para salvar. Porque ao executar o programa de novo, ele vai ler o jsonq  estava com a lista salva,
    # e tarefas vai ter os itens, puxados do JSON
    print()
    if not tarefas:
        print('Nenhuma tarefa para exportar')
        return
    with open("aula119b.json", "w", encoding="utf-8") as arquivo:
        # fazer dump() diferente de dumpas()
        json.dump(tarefas, arquivo,indent=2) # ensure_ascii=false, caso nao queira q acentos virem u0100 etc
        # json nao pega funções, classes, ou sets. Mas coisas convertidas sim.
        # uma tupla vira uma lista no json, ent ao converter de volta será uma lista
    print("Tarefas exportadas.")

"""
LUIZ OTAVIO:

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

"""

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, clear e exportar')
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
    elif tarefa == 'exportar':
        exportar(tarefas)
        # salvar(tarefas, CAMINHO_ARQUIVO) # Luiz Otavio
        break
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue