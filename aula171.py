# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count
caminho = os.path.join("C:\\","Users","Pepe","Pictures","nepnepemotes")
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, " ",root)

    for dir_ in dirs:
        print("  ",the_counter, "Dir pintor: ",dir_)

    for file_ in files:
        print("  ",the_counter, "File: ", file_)
        # caminho_completo = os.path.join(root, file_)
        # print("  ",the_counter, "File: ", caminho_completo)
        # NAO RODAR SEM PENSAR:
        #   é possível  dar os.unlink(caminho_completo) para remover os arquivos
        