print('-=-' * 12)
print('{:^36}'.format('10 Primeiros termos de uma PA'))
print('-=-' * 12)
primeiro_termo = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))

for n in range(10):
    termo = primeiro_termo + razão *  n
    print('O {}º termo da PA é: {}'.format(n + 1, termo))