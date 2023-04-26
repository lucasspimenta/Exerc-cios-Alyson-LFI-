"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor. 
"""

custo_fabrica = int(input('O valor gasto com material e mão de obra para a produção do carro foi de: R$ '))
custo_imposto = custo_fabrica * 0.45
custo_distribuidor = custo_fabrica * 0.28
custo_final = custo_fabrica + custo_distribuidor + custo_imposto

print(f'O custo final do carro é de: R${custo_final}')


