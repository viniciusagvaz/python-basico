def multiplicador(numero):
        a1 = 2 # esta variável tem escopo local
        print(f"- Dentro da função, a variável 'a1' vale: {a1}")
        return a1 * numero

a1 = 3 # esta variável tem escopo global
print(f"- Fora da função, a variável 'a1' vale: {a1}")

b1 = multiplicador(5)
print(f"- A variável 'b1' vale: {b1}")



def multiplicador2(numero):
        global a2 # todas as referências à variável a são para a global
        a2 = 1      # a global será alterado
        print(f"- Dentro da função, a  variável 'a2'  vale: {a2}")
        return a2 * numero


a2 = 3  # esta variável tem escopo global
b2 = multiplicador2(6)
print(f"- A variável 'b2' vale: {b2}")
print(f"- Fora da função, a variável 'a' vale: {a2}")