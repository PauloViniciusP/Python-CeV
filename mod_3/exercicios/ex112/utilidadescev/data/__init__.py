def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()

        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m]')
        else:
            valido = True
            return float(entrada)
        

# def leiaInt(msg):
#     check = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             check = True
#         else:
#             print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
#         if check:
#             break
#     return valor
