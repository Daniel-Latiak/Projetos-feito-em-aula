"""
Repetiçoes
while (enquanto)
Executa uma açao enquanto uma condiçao for verdadeira
"""
condicao = True

while condicao:
    nome = input('qual é seu nome :')
    print(f'seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')