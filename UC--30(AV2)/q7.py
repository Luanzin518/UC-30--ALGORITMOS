while True:
    print("
1 - Soma")
    print("2 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 + n2)
    elif opcao == 2:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.") )