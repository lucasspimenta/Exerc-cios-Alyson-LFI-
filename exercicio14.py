Pão = int(input('Quantida de pão vendidos:'))
Bolo = int(input('Quantidade de bolos vendidos:'))
Valor_pão = Pão*0.12
Valor_bolo = Bolo*1.50
Vendas = Valor_pão+Valor_bolo
Guardar = Vendas*(10/100)
print(f'Foram vendidos {Vendas} reais de pães e bolos. Deverá ser guardado {Guardar:.2f} reais')