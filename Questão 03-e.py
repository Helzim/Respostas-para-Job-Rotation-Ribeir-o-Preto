# Alternativa (e) apresenta uma sequencia de fibonacci
n = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Inicializa os primeiros termos da sequência
a, b = 0, 1

# Imprime os n termos da sequência de Fibonacci
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
