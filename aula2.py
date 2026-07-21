# print (args[1,2,3,...], padrão da função print, bota um espaço entre, ao exibir mais de um texto como argumento,vulgo args[])
print(12,34) # são chamados de argumentos não-nomeados. Argumentos NOMEADOS podem ser usados pra mudar isso.
# truque do vscode: ctrlc] + c e ctrl + v sem selecionar NADA duplica a linha
# mais padrão, após um print, ele tem quebra de linha, diferente de C ou java q precisa por println
print(56,78)

# argumentos nomeados. Sep = Separador:
print(12,34, 1011, sep="-") 
print(56,78,sep='-') 
print(9,10,sep='-') 

# CRLF = carriage return line feed = quebra de linha específica do windows
# \r\n RETURN e N É LINE FEED
# no mac, linux, unix é só LF (\n)

print(12,34, 1011, sep="-", end='\n##\n') 
print(56,78,sep='-',end='\n') 
print(9,10,sep='-',end='\n') 

# python é case sensitive, Print() não funciona, dá um NameError, python é bom de explicar erros