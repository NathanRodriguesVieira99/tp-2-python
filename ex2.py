def analisar_promocao(tempo_empresa_ano: int, nota_avaliacao: float, carga_horaria: int) -> str:

    if tempo_empresa_ano > 2 and nota_avaliacao >= 8.0:
        return 'Elegível para promoção'
    else:
        return 'Aguardando próxima avaliação'


print(analisar_promocao(3, 8.5, 40))
