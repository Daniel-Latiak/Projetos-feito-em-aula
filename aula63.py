# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria','Helena', 1,2,3,'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0,
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine'  ], # 1 
    # 0        1         2
    ['Luiz', 'Joao', 'Eduarda',], # 2
]
# p,b,*_,ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome , end= ' ', sep=' ')

# print('Maria','Helena', 1,2,3,'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# print(*salas, end='\n')
print(*salas, sep='\n')
