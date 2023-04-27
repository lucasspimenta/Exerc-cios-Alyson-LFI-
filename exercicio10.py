Nome = input('Informe seu nome:')
Salario_mensal = float(input('informe seu salário mensal:'))
Vendas = float(input('Informe o total de venda em reais:'))
comissao = 15/100*(Vendas)
S_final = comissao+Salario_mensal
print(f'{Nome}, seu salário mensal é de {Salario_mensal}, somados com sua comissão, você receberá {S_final} reais.')