animal= ["cachorro," "gato"]
print ("lista inicial: ", animal)

animal. append("pato") #adiciona  no fim da lista
print ("lista atualizada:", animal)

animal.insert(1, "coelho")
print("lista atualizado: ", animal)

animal.extend(["macaco","leão"])#add mais um dado
print("lista atualizada", animal)

animal.remove("leão")
print(animal)

removido = animal.pop()
print(f"removido: {removido}")
print("após pop()", animal)

removido2 = animal.pop(1)
print(f"removido do indice 1 {removido2}")
print("após pop(1):", animal)

del animal[0]
print("após o del", animal)

animal.clear()
print(animal)