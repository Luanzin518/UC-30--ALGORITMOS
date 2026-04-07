import random

def jogo_adivinhacao():
    print("\n" + "=" * 40)
    print("JOGO DE ADIVINHAÇÃO")
    print("=" * 40)
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Tente adivinhar o número entre 1 e 100!")
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100!")
                tentativas -= 1
                continue
            
            if palpite < numero_secreto:
                print("MAIOR")
            elif palpite > numero_secreto:
                print("MENOR")
            else:
                print(f"\n🎉 Parabéns! Você acertou em {tentativas} tentativas!")
                break
                
        except ValueError:
            print("Por favor, digite um número válido!")

def analisar_numeros():
    print("\n" + "=" * 40)
    print("ANALISADOR DE NÚMEROS REPETIDOS")
    print("=" * 40)
    
    numeros = []
    
    for i in range(1, 9):
        while True:
            try:
                numero = int(input(f"Digite o {i}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número válido!")
    
    contagem = {}
    for numero in numeros:
        contagem[numero] = contagem.get(numero, 0) + 1
    
    print("\n" + "=" * 40)
    print("RESULTADOS")
    print("=" * 40)
    
    tem_repetidos = False
    for numero, quantidade in contagem.items():
        if quantidade > 1:
            tem_repetidos = True
            print(f"🔁 Número {numero} apareceu {quantidade} vezes")
    
    if not tem_repetidos:
        print("✅ Nenhum número foi repetido!")
    
    print(f"\n📊 Total de números únicos: {len(contagem)}")

def main():
    while True:
        print("\n" + "=" * 40)
        print("MENU PRINCIPAL")
        print("=" * 40)
        print("1 - Jogo de Adivinhação")
        print("2 - Analisador de Números")
        print("3 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            jogo_adivinhacao()
        elif opcao == "2":
            analisar_numeros()
        elif opcao == "3":
            print("\n👋 Obrigado por usar o programa! Até mais!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

# Executar o programa principal
if __name__ == "__main__":
    main()