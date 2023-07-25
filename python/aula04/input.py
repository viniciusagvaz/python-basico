# Entrada de dados com a função Input()
# Quando o programador quiser que o usuário entre com algum valor, ele deverá exibir na tela o seu pedido. Em C, é necessário utilizar a função printf() para escrever a solicitação ao usuário e a função scanf() para receber a entrada e armazenar em uma variável. Em Python, é possível utilizar a função input(). Ela tanto exibe na tela o pedido, como permite que o valor informado pelo usuário seja armazenado em uma variável do seu programa. Analise a imagem seguinte:

nome = input('Entre com seu primeiro nome: ')
print(nome)

# A linha 1 fará com que a frase Entre com seu nome: seja exibida no console, mas a execução do programa fica travada até que o usuário aperte [ENTER] no teclado. Tudo o que foi digitado até o [ENTER] vai ser armazenado na variável nome. A linha 2 fará a exibição do conteúdo da variável nome.

# Atenção!
# É importantíssimo perceber que a função input() trata tudo o que for digitado pelo usuário como uma string, armazenando na variável designada pelo programador para isso. Mesmo que o usuário entre com apenas uma letra ou um número, isso será armazenado como uma string na variável.

numero = input('Entre com um número inteiro: ')
# print(numero + 2) 
# print(type(numero))