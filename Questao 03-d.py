# Alternativa (d) apresenta o quadrado dos numeros pares
n = int(input("Digite um número: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i ** 2)