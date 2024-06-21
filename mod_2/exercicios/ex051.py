print('-=-' * 12)
print('{:^36}'.format('10 Primeiros termos de uma PA'))
print('-=-' * 12)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
decimo_termo = primeiro + (10 - 1) * razão

for n in range(primeiro, decimo_termo + razão, razão):
    print('{}'.format(n), end=' -> ')
print(' End')