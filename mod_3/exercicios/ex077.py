palavras = ('Aprender', 'programar', 'linguagem', 'python', 'curso',
            'grátis', 'praticar', 'estudar', 'mercado', 'trabalhar',
            'programador', 'futuro', 'presente')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáãâàeéêiíou':
            print(letra, end=' ')