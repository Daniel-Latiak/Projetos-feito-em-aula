"""
intoduçao ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input(
    'vou dobrar o numero que voce digitar: '
    )

try:
    print('STR:',numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print('isso nao é um numero')

#if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.0f}')
#
#else:
#     print('isso nao é um numero')