numero=int(input('Digite o numero inteiro: '))
binario=""

while numero>0:
    binario+=str(numero%2)
    numero//=2

print(f'O numero binario é: {binario[::-1]}')