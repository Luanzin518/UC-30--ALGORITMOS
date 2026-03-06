notas = [7.5,8.0,9.5,6.0,8.5]
print("notas: ", notas)

print("menor nota: ", min(notas))
print("menor nota: ", max(notas))
print("soma: ", sum(notas))
print("média: ", sum(notas) / len(notas))



nomes = ["Adriana", "barbara", "Carla", "Daniel"]

print("Usando FOR simples:")

for nome in nomes:
    print(f"olá, {nome}")
    print("usando enumerate:")# indice e elemento

for indice, nome in enumerate(nomes):
    print(f"posição {indice}: {nome}")

    original = ["A","B","C"]
    copia = list(original)

    print("original: ", original)
    print("copia:", copia)
    print("são iguais:", original == copia)

    copia.append("D")
    print("original: ", original)
    print("cópia: ", copia)
    print("são iguais: ",original == copia)