lista = []

for c in range(15):
    usuario = []

    altura = float(input('Digite a sua altura: '))
    genero = input('Digite o seu gênero: ')

    usuario.append(altura)
    usuario.append(genero)

    lista.append(usuario)


menor = lista[0][0]
maior = lista[0][0]

for c in lista:
    if c[0] < menor:
        menor = c[0]

    if c[0] > maior:
        maior = c[0]


soma = 0
quantidade_masc = 0
quantidade_fem = 0

for c in lista:

    if c[1] == 'masculino':
        soma = soma + c[0]
        quantidade_masc = quantidade_masc + 1

    elif c[1] == 'feminino':
        quantidade_fem = quantidade_fem + 1


media = soma / quantidade_masc


print(f'A maior altura do grupo é: {maior}')
print(f'A menor altura do grupo é: {menor}')
print(f'A média de altura das pessoas masculinas é: {media}')
print(f'O número de pessoas do gênero feminino é: {quantidade_fem}')
