# try execpt else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print("Abrir aquivo")
    # 8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print("Dividido por zero")
except IndexError as error:
    print("indexerror")
except (NameError, ImportError) as error2:
    print("name ou index error")
else:
    print("Executado caso não ocorra erros")

finally:
    # close file
    print("fechar arquivo") # o finally foi executado mesmo q tenha tido um erro não tratado