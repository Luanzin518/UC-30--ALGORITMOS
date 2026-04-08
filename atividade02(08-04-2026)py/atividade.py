def verba_do_joao(gastos_do_mes, mesada):
    # somando na mão porque esqueci que existe sum()
    total = 0
    for conta in gastos_do_mes:
        total = total + conta  # dá pra fazer += mas assim fica mais explicado
    
    print("Total de gastos: R$", total)
    print("Mesada: R$", mesada)
    
    if total < mesada:
        resto = mesada - total
        print("João, você conseguiu economizar R$", resto, "! Bom menino")
    elif total > mesada:
        falta = total - mesada
        print("Eita, João gastou R$", falta, "a mais. Hora de cortar os lanches")
    else:
        print("Fechou certinho, nem sobrou nem faltou")