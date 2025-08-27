# F1 -> falha de inicialização do motor
# F2 -> superaquecimento do painel elétrico
# F3 -> oscilação na temperatura da esteira
# F4 -> erro de leitura dos sensores ópticos
# Tempertura pode variar entre 20 e 80 graus

def verificar_falhas_linha_de_montagem(codigo: str, temperatura: int) -> str:
    if codigo == 'F1' and temperatura < 40:
        return 'Reiniciar Máquina'
    elif codigo == 'F2' and temperatura > 60:
        return 'Verificar conexão elétrica e sistema de refrigeração'
    elif codigo == 'F3' and temperatura > 45 or temperatura < 55:
        return 'Ajustar temperatura da esteira'
    elif codigo == 'F4':
        return 'Realizar diagnóstico dos sensores ópticos'
    else:
        return 'Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável'


print(verificar_falhas_linha_de_montagem('F2', 30))
