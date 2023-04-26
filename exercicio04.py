"""
Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto 
"""

distancia = float(input('A distância percorrida, em quilômetros, foi de: '))
consumo = float(input('O consumo total de combustível, em litros, foi de:  '))

consumo_medio = distancia / consumo

print(f'O consumo médio do automóvel foi de: {consumo_medio} km/l.')

