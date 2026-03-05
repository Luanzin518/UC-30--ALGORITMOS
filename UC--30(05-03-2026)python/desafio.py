import random
numeros = [49,18,79,93,36]
print("Lista inicial:", numeros)

# sort crescente
numeros.sort()
print("Após sort():", numeros)

# sort decrescente
numeros.sort(reverse=True)
print("Após sort():", numeros)

#embaralhar
dados = [1,2,3,4,5]
random.shuffle(dados)
print("Embaralhar: ", dados)
