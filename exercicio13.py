Custo = float(input('informe o preço de custo:'))
Margem = float(input('informe a porcentagem de lucro do produto:'))
Porcentagem = (Margem/100)*Custo
Preço_venda = Porcentagem+Custo
print(f'O preço de venda será de:{Preço_venda:.2f} reais')