# Formatação de dados de saída
# Quando desejamos que a saída siga determinado padrão – por exemplo, de hora ou de data – existem algumas possibilidades para usar a função print(). É sempre possível utilizar a concatenação de strings, com o operador +, para montar a frase como quisermos. Suponha que tenhamos as seguintes variáveis:

hora = 10
minutos = 26
segundos = 18

# Poderíamos chamar a função print() com o separador: da seguinte forma:

print(str(hora) + ":" + str(minutos) + ":" + str(segundos))


# Porém, existe outra possibilidade, usando o método format(). Ele permite que a chamada à função print() fique muito parecida com as chamadas à função printf() em C, com passagem de parâmetros a serem colocados em ordem na string. Com o método format(), podemos montar a string com as chaves {} indicando onde entrarão valores, passados como parâmetros separados por vírgulas, como mostrado na imagem abaixo:

print("{}:{}:{}".format(hora, minutos, segundos))


# É importante observar que a quantidade de chaves precisa ser igual à quantidade de variáveis passadas como parâmetros no método format(). Seria muito bom se não precisássemos nos preocupar com essa correspondência para evitar erros bobos. E isso é possível! Para tornar a saída formatada ainda mais intuitiva, basta utilizar a letra ‘f’ no início dos parâmetros da função print() e colocar cada variável dentro das chaves na posição em que deve ser impressa. Veja como fica ainda mais fácil entender:

print(f'{hora}:{minutos}:{segundos}')


# Também é possível especificar a largura de campo para exibir um inteiro. Se a largura não for especificada, ela será determinada pela quantidade de dígitos do valor a ser impresso. Confira na imagem:

print('{:4}, {:5}'.format(10, 100))

# Observe acima que os valores 10 e 100 foram impressos com espaços em branco à esquerda. Isso ocorreu porque definimos que a primeira variável deveria ser impressa com 4 espaços com {:4} (2 foram ocupados e 2 ficaram em branco), e que a segunda variável deveria ser impressa com 5 espaços com {:5} (3 foram ocupados e 2 ficaram em branco).


# O método format() também pode ser usado para imprimir valores de ponto flutuante com a precisão definida. Vamos a mais um exemplo:

print('{:8.5}'.format(10/3))

# Ao usar {:8.5}, estamos determinando que a impressão será com 8 espaços, mas apenas 5 serão utilizados.


# Impressão de sequências
# Python também permite a impressão de sequências com mais possibilidades que C, incluindo as strings. Para imprimir um vetor em C, por exemplo, precisamos chamar a printf() item a item. Em Python, basta chamar a função print() passando como parâmetro a sequência, veja:

seq = [0, 1, 2]
print(seq)


# Para imprimir uma substring, por exemplo, basta utilizar os colchetes para indicar o intervalo de índices que deve ser impresso. Vale lembrar que o primeiro caractere da string é indexado com 0. Confira na imagem:

str = 'Hello World'
print(str[0:4])
print(str[2:8])