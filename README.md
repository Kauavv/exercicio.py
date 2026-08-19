lista=[]

for c in range (3):
    usuario=[]
    altura=float(input('Digite a sua altura: '))
    genero= input('Digite o seu gênero: ')
    usuario.append(altura)
    usuario.append(genero)
    lista.append(usuario)
menor=(lista[0][0])
maior=(lista[0][0])
for c in lista:
    if c[0] < menor:
        menor = c[0]
    if c[0] > maior:
        maior = c[0]
soma=(0)
quantidade_masc=(0)
quantidade_fem=(0)
for c in lista:
    if c[1] == 'masculino':
        soma = soma + c[0]
        quantidade_masc = quantidade + 1
    elif c[1] == 'feminino':
        quantidade_fem=+ 1 
media=soma/ quantidade
quantidade_fem=(0)

print(f'A maior altura do grupo é: {maior}')
print(f'A menor altura do grupo é: {menor}')
print(f'A media de altura ds pessoas masculinas é: {media}')
print(f'O número de pessoas do genero feminino é: {quantidade_fem}')
