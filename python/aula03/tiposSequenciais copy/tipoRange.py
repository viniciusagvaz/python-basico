# Range
# O tipo range representa uma sequência imutável de números e frequentemente é usado em loops de um número específico de vezes, como o for.

# Ele pode ser chamado de maneira simples, apenas com um argumento. Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive). Por exemplo, range(3) cria a sequência (0, 1, 2).

# Para que a sequência não comece em 0, podemos informar o início e o fim como parâmetros, lembrando que o parâmetro fim não entra na lista (exclusive o fim). O padrão é incrementar cada termo em uma unidade. Ou seja, a chamada range(2, 7) cria a sequência (2, 3, 4, 5, 6).

print(list(range(5)))
print(list(range(2, 7)))

# Também é possível criar sequências mais complexas, indicando os parâmetros de início, fim e passo, nessa ordem. O passo é o valor que será incrementado de um termo para o próximo. Por exemplo, range(2, 9, 3) cria a sequência (2, 5, 8).

print(list(range(2, 9, 3)))

