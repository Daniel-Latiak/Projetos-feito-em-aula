"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Clara'), (1, 'Daniel'), (2, 'Amor'), (3, 'latiak')]
lista = ['Clara','Daniel', 'Amor']
lista.append('latiak')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')