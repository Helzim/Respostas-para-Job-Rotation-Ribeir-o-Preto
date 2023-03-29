# Codigo que responde o problema solicitado

# Distância entre Ribeirão Preto e Franca em km
distancia = 100
# Velocidade do carro em km/h
velocidade_carro = 110
# Velocidade do caminhão em km/h
velocidade_caminhao = 80
# Tempo que o caminhão leva a mais para passar em cada pedágio
tempo_pedagio = 5  # em minutos
# Converter tempo do pedágio para horas
tempo_pedagio = tempo_pedagio / 60
# Distância que o carro percorre até encontrar o caminhão
distancia_encontro = distancia / 2
# Tempo que o carro leva para encontrar o caminhão
tempo_encontro = distancia_encontro / velocidade_carro
# Tempo que o caminhão leva para encontrar o carro
tempo_encontro_caminhao = distancia_encontro / velocidade_caminhao
# Acrescentar tempo dos pedágios ao tempo do caminhão
tempo_encontro_caminhao += 2 * tempo_pedagio

if tempo_encontro < tempo_encontro_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
