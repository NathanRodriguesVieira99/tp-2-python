notas_avaliacao = [5, 8, 10, 6, 9, 4]

def avaliar_notas(notas):
    return [nota for nota in notas if nota >= 7]

print(avaliar_notas(notas_avaliacao))
