
N = int(input())
R = int(input())
P = int(input())

total = N
novos = N
dias = 0

print("Começamos com", total, "pessoas infectadas no dia zero.")

while total < P:
    dias = dias + 1
    novos = novos * R
    total = total + novos
    print("No dia", dias, "mais", novos, "pessoas foram infectadas, chegando a um total de", total, "pessoas.")

print("Serão necessários", dias, "dias para atingir ou ultrapassar o número alvo.")
print(dias)