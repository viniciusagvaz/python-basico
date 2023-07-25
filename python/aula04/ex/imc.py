# Como exercício prático, tente escrever um programa para calcular e informar o IMC (índice de massa corpórea) do usuário, que deverá fornecer seu peso e sua altura. Lembre-se de que o IMC é calculado pela fórmula: IMC = peso/altura²


p = eval(input('Entre com seu peso: '))
a = eval(input('Entre com sua altura(cm): '))
imc = (p/(a**2))*10000

print(f'IMC = {imc}')
