# A função eval()
# A função eval() recebe uma string, mas trata como um valor numérico. Veja o exemplo:

s = '1 + 2'
print(type(s))
print(eval(s))

# Mesmo tendo recebido a string ‘1+2’ como parâmetro, a função eval() efetuou a soma de 1 com 2. Observe que confirmamos que s é uma string com a instrução type(s).

# Para tratar a entrada do usuário como um número e, com isso, realizar operações algébricas, por exemplo, é necessário utilizar a função eval() em conjunto com a input(), veja:

numero = eval(input('Entre com um número inteiro: '))
numero += 2
print(numero)