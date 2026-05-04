soma = 0

while True:
    valor = float(input("Digite um valor (0 para parar): "))
    if valor == 0:
        break
    soma += valor

print("Total:", soma)