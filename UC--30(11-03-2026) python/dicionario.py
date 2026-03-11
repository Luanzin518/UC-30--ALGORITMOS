contato = {
    "@camila": "camila",
    "@paola" : "paola",
    "@sheron" : "sheron",
    "@bruna" : "bruna",
    "@joao" : "joao"
}
# obter chaves
print("chaves: ")
for insta in contato.key():
    print(insta)


print("\n valores:")
for nome in contato.values():
     print(nome) 

#obter pares (chaves-valor)
print("\ pares:")
for insta, nome in contato.items():
     print(f"{insta} --> {nome}")    

contato = {
     "@camila": 1.66,
    "@paola" : 1.50,
    "@sheron" : 1.80,
    "@bruna" : 1.60,
    "@joao" : 1.70
}



     #ordenar por chave
print("ordenar por chaves")
for insta in sorted(contato.keys()):
    print(f"{insta}--> {contato[insta]:.2f}m")     


    #ordenar por valor
from operator import itemgetter
print("\n ordenando por valor (altura):")
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
     print(f"{insta}--> {estatura: .2f}m")
