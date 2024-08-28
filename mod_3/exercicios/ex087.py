total = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somatcol = maiorscol = 0

for l in range(0, 3):
    for c in range(0, 3):
        total[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))
        if total[l][c] % 2 ==0:
            somaPar += total[l][c]
        if c == 0 or total[1][c] > maiorscol:
            maiorscol = total[1][c]
    somatcol += total[l][2]

print('-=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{total[l][c]:^5}]', end='')
    print()

print('-=-' * 15)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somatcol}')
print(f'O maior falor da segunda linha é {maiorscol}')
