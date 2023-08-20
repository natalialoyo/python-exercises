x = input('Digite algo: ')
print(f'O tipo primitivo deste valor é: {type(x)}')
print(f'O valor tem apenas espaços? {x.isspace()}')
print(f'O valor é um número? {x.isnumeric()}')
print(f'O valor é alfabético? {x.isalpha()}')
print(f'O valor é alfanumérico? {x.isalnum()}')
print(f'O valor está em letras maiúsculas? {x.isupper()}')
print(f'O valor está em letras minúsculas? {x.islower()}')
print(f'O valor está capitalizado? {x.istitle()}')

    # NO VÍDEO O COMANDO PRINT É USADO COMO NOS MODELOS ABAIXO:
    # print('O tipo primitivo deste valor é: ', type(x))
    # print('O valor tem apenas espaços? ', x.isspace())
