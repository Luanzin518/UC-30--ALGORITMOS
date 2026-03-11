# QUESTÃO 8
compra = float(input("Valor da compra: "))

if compra < 100:
    desc = 0
elif compra < 500:
    desc = compra * 0.05
elif compra < 1000:
    desc = compra * 0.10
else:
    desc = compra * 0.15

valor_final = compra - desc

print("Valor da compra:", compra)
print("Desconto:", desc)
print("Total a pagar:", valor_final)
