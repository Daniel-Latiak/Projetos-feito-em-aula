nome = 'DANIEL'
altura = 1.88
Peso = 83
imc =23.48347668628339  # IMC = peso / (altura x altura)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura, '
linha_2 = f'pesa {Peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
# Daniel tem 1.88 de altura
# pesa 83 quilos e seu imc é
# 23.48347668628339