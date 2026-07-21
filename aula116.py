import os # explicação linha 84
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# caminho_arquivo = 'aula116.txt'
# ou
# temq  usar duas barras para caminhos Windows
caminho_arquivo = 'C:\\Users\\Pepe\\Documents\\pyLearning1\\arquivos\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'r') # se nao existir, o r dá exception de file not found

# arquivo = open(caminho_arquivo, 'w') # w, porém, cria o arquivo caso ele nao exista
# # # ao abrir, (sem with) JA FECHA com comando no final. Nao deixa arquivo aberto pq pode deixar problema
# # ao usar with, porém, ele ja usa e fecha
# arquivo.close()


# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')

# try except finally. Finally com o arquivo.close() hehe

# da terceira aula:
# interessante: ao abrir com w. O módulo apaga oq tá no arquivo e escreve de novo

# com with:
# with open(caminho_arquivo, "w+") as arquivo:
#     # print(type(arquivo))
#     # print("Hola q tal")
#     # print("Arquivo vai ser fechado")
#     # dá pra mover o cursor dentro do arquivo usando SEEK, mas luiz nao usa isso
#     arquivo.write("Linha 1\n") # se preciso, colocar quebra de linha, ele nao bota linha por linha a cada comando (windows: \r\n, mac: \n??? \n funfou no win)
#     # ao abrir o arquivo no vscode tb, fica fácil de ver se as alterações foram realizadas.
#     arquivo.write("Linha 2\n")
#     arquivo.writelines( # útil para escrever um iterável
#         ("Linha 3\n","Linha 4\n")
#         )
#     arquivo.seek(0,0) # tem q mover pra ler do começo de novo
#     # arquivo.write("Linha 3\n")
#     print(arquivo.read()) # com w+, read funciona com write na mesma operação de open()
#     print("Lendo")
#     arquivo.seek(0,0)
#     print(arquivo.readline(), end = "") # readline é tipo um next(). end para nao quebrar mais uma linha na hora do print
#     print(arquivo.readline().strip())
    
#     print("READLINES")
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# print("#" * 10)

with open(caminho_arquivo,"a+") as arquivo: # com a (append) ele adiciona mais ao fim do arquivo
    arquivo.write("Atenção\n")
    # arquivo.write("Linha 1\n")
    # arquivo.write("Linha 2\n")
    # arquivo.writelines( 
    #     ("Linha 3\n","Linha 4\n")
    #     )
    arquivo.write("MÉÉÉÉTIO\n") # caraccteres com acento em windows precisa confirmar o encoding (UTF-8)
    # escrever no arquivo de texto, mas ao abrir ele no vscode para conferir, clicar la em baixo no UTF-8 e la em cima "reopen with encoding"
    # utilizar Windows 1252 (deve ser esse, foi no do luiz e no meu).
    # OU, vc coloca enconding no with open()
    # with open(caminho_arquivo,"a+", encoding="utf-8") as arquivo: # ou encoding="utf8"
    
# agora sobre os . os.remove rename etc
# os.unlink(caminho_arquivo) # remover arquivo
# os.remove(caminho_arquivo) # remover arquivo

# os.rename(caminho_arquivo, "aula116-2.txt")

