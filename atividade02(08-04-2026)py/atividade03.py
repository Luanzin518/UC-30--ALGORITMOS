def internet_do_lucas(consumo_por_dia):
    limite_plano = 30  # 30 gigas, o resto é choro
    
    # somando os dias um por um (igual Lucas faria no papel)
    total_usado = 0
    for dia in consumo_por_dia:
        total_usado = total_usado + dia
    
    print("Consumo total do mês:", total_usado, "GB")
    
    if total_usado > limite_plano:
        excedeu = total_usado - limite_plano
        print("LASCOU! Lucas passou em", excedeu, "GB. A internet vai ficar lenta")
    else:
        sobra = limite_plano - total_usado
        print("Ufa! Ainda sobram", sobra, "GB. Pode ver vídeo sim")