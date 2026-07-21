# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# apagar -> os.unlink
# apagar recursivamente -> shutil.rmtree
import os
import shutil

caminho = os.path.join("C:\\","Users","Pepe")
HOME = os.path.expanduser(caminho)
DESKTOP = os.path.join(HOME, "Desktop") # HOME+"\\Desktop"
# print(HOME)
PASTA_ORIGINAL = os.path.join(DESKTOP, "imgteste")
# print(os.path.exists(PASTA_ORIGINAL))
NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")
# print(NOVA_PASTA)
os.makedirs(NOVA_PASTA, exist_ok = True) # cria pasta

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_pintor in dirs:
        caminho_novo_dir = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA),  dir_pintor)
        # print(caminho_novo_dir)
        os.makedirs(caminho_novo_dir, exist_ok = True)
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA),  file_)
        # print(caminho_novo_arquivo)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
        # print(file_)