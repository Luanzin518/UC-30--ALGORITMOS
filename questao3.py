resposta = input("Você tem uma carteira de motorista? (s/N):")

possui_cnh = resposta.strip().lower() =="S"

print("Valor:", possui_cnh)
print("Tipo:", type(possui_cnh))