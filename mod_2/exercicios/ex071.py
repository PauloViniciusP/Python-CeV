print('=' * 30)
print('{:^30}'.format('Banco Bão Demais'))
print('=' * 30)

valor = int(input('Qual valor deseja sacar? R$'))

total = valor
cedula = 50
totcédula = 0

while True:
    if total >= cedula:
        total -= cedula
        totcédula += 1
    else:
        if totcédula > 0:
            print(f'Total de {totcédula} cedulas de R${cedula}')
   
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totcédula = 0

        if total == 0:
            break

print('=' * 30)
print('Obrigado e volte sempre ao Banco Bão Demais.')
