# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    except Exception as e:     # pode ser somente try e finally tb
        print("O correu erro:", e)
        
    finally:
        print("Fechando arquivo")
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    # arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)