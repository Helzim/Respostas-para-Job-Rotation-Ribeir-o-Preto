# Alternativa (a) imprime numeros impares. Segue o exemplo:
n = int(input("Digite um número inteiro positivo: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
