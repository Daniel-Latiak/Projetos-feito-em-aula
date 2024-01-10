"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# nome = 'Daniel'
# idade = int(19)
# variavel = '%s sua idade é %i' % (nome, idade)
# print(variavel)

# if nome and idade:
#     print = ('seu nome é', nome)





nome = input('digite meu nome: ')
idade = input('digite minha idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print (f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
      print (f'seu nome contém espaços')
    else:
     print (f'seu nome Nao contém espaços')

    print (f'seu nome tem", {len(nome)} leras')
    print (f'a primeira letra do seu nome é: {nome[0]}')
    print (f'a ultima letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou espaços em branco.')