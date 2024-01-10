# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  d a n i e l
# -6-5-4-3-2-1

#nome = 'daniel'
#print(nome[2])
#print(nome[-4])
#print('dani' in nome)
#print('el' not in nome)

nome = input('digite seu nome: ')
encontrar = input('digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar}esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
