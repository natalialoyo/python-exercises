km = float(input('Quantos quilômetros seu carro percorreu? '))
dias = int(input('Quantos dias ele foi alugado? '))
val = 60 * dias + 0.15 * km
print(f'O valor a ser pago pelo aluguel do veículo é R${val:.2f}.')
