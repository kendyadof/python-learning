# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# C:\Users\Pepe\Pictures\gigimurin
import os
# caminho = r"C:\\Users\\Pepe\\Pictures\\gigimurin"
caminho = os.path.join("C:\\","Users","Pepe","Pictures","nepnepemotes")
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho,pasta)
    if not os.path.isdir(caminho_completo):
        continue
    for imagem in os.listdir(caminho_completo):
        print(caminho_completo,imagem)