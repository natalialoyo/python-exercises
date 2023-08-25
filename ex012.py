val = float(input('Digite o valor do seu produto: '))
desc = val - (val * 5 / 100)
print(f'Com 5% de desconto, seu produto custará R${desc:.2f}.')
