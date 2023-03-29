# Solicita o número para o úsuario
numero = int(input("Digite o numero que deseja: "))
sequencia_fibonacci = [0, 1]

# Inicia a sequência de Fibonacci
while sequencia_fibonacci[-1] < numero:
    proximo = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
    sequencia_fibonacci.append(proximo)

# Verifica se o número digitado está na sequência
if numero in sequencia_fibonacci:
    print(f"O numero {numero} está na sequência de fibonacci.")
else:
    print(f"O numero {numero} não está na sequência de fibonacci.")
