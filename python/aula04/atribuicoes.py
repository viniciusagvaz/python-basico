# Atribuição simples:
# Chamamos de atribuição simples a forma que já utilizamos neste conteúdo, com uma expressão parecida com x = 10. Nessa atribuição, a variável x recebe o valor 10.

x = 10
print(x)

# Atribuição múltipla:
# Python também permite a atribuição múltipla, ou seja, mais de uma variável receber atribuição na mesma linha. A título de exemplo, clique em Executar no emulador abaixo:

x, y = 2, 5
print(x)
print(y)

# Operadores de atribuição compostos:
# Os operadores de atribuição compostos executam operações matemáticas e atualizam o valor da variável utilizada. Veja no código abaixo (clique em Executar):

x = 10
x = x + 1
print(x)

# Troca de variáveis:
# Um dos problemas iniciais que envolvem atribuição de valores a variáveis é a troca entre duas delas. Suponha que as variáveis a e b armazenem, respectivamente, os valores 1 e 2. Caso quiséssemos inverter os valores em linguagens como C ou Java, seria necessário usar uma variável auxiliar. Em Python, é possível fazer essa troca de uma maneira muito mais fácil, com o uso da atribuição múltipla. Veja no código abaixo (clique em Executar) as duas maneiras de se trocar valores entre 2 variáveis, através do uso de variável auxiliar e através de atribuição múltipla, veja:

a = 1
b = 2

# troca de variáveis usando variável auxiliar ‘temp’

temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla

a, b = b, a
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")