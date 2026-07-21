a = 'AAAAA'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
# tudo em python é objeto, ao botar um ponto dps, mostra todos os métodos desse objeto
# botar nome da variavel do argumento ={} , chaves abre e fecha, ele mostra o valor de cada uma
# {:.2f} por exemplo mostra 2 casas decimais

print(formato)


formato = 'a={0} a={0} a={0} a={0} b={1} c={2:.2f}'.format(a, b, c)
# pode-se utilizar os ÍNDICES dentro das chaves, indíces da sequência de argumentos
# a  b c = parâmetro nomeado = vc q pode dar o nome.
# a partir do momento q se dá nome, tudo dps tem q ser nomeado

# Se botar nome3 ao inves de c, vai dar erro out of range se nao colocar nome1 e nome2
print(formato)

formato = 'a={0} a={0} a={0} a={0} b={1} c={nome3:.2f}'.format(a, b, nome3=c)
# ao colocar nome3=c, o "nome3" precisa ser chammado dentro da chave q está no c, dentro da string "formato"
# agora o "nome3" é um parâmetro, pq está se referindo ao nome da variável
# quando se refere ao valor de c, isso é chamado argumento. a e b = argumento, nome3 = parâmetro
print(formato)

formato = 'b={nome2} a={nome1} a={nome1}  c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)
# inverteu a e b arbitrariamente
print(formato)