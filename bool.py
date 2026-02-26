#resp = input("Você vai passar de ano? s/n")
#resultado = bool(resp)

#print("resultado", resultado)
#print("resposta",resp)


resp = input("Você vai passar de ano? s/n: ").strip().lower()
resultado =resp in ("s;""sim")

print(type("resultado"))
print("resultado", resultado)