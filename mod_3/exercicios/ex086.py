matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input(f'Digite o valor para [{i+1}, {j+1}]: '))
print('-=-' * 10)

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end='')
    print()
