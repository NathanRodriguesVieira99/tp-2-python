def avaliar_risco(distancia_km: int, clima: str, zona_entrega: str) -> str:
    if distancia_km > 300 and clima == 'chuva' or zona_entrega == 'rural':
        return 'Risco de atraso'
    else:
        return 'Entrega dentro do previsto'


print(avaliar_risco(300, 'chuva', 'rural'))
