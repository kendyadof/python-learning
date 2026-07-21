# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / "aula179.csv"

# with open(CAMINHO_CSV, "r") as arquivo:
#     leitor = csv.reader(arquivo)
#     # next(leitor)
#     # print(next(leitor))
#     for linha in leitor:
#         print(linha)

# em forme de dicionário:
with open(CAMINHO_CSV, "r") as arquivo: 
    leitor = csv.DictReader(arquivo)
    # next(leitor)
    # print(next(leitor))
    for linha in leitor:
        print(linha["Nome"], linha["Idade"], linha["Endereço"])