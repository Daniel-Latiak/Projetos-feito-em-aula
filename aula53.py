"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Daniel','Nilza', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)











# nome = 'DANIEL'
# noutra_variavel = nome
# nome ='Nilza'
# print(nome)
# print(noutra_variavel)