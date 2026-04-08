def custo_busao(preco_passagem, dias_de_aula):
    # ida e volta, né? Maria não é teletransportada
    passagens_por_dia = 2
    total_passagens = dias_de_aula * passagens_por_dia
    grana_gasta = preco_passagem * total_passagens
    
    print("Maria, você vai gastar R$", grana_gasta, "nesse período todo")
    print("(Isso dá", total_passagens, "passagens no total)")