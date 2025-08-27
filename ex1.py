ANO_2_DIGITOS = 5

def analisar_transacao(valor, tipo):
    if valor > 1000 * ANO_2_DIGITOS and tipo == "transferência":
        print("Alerta: verificar origem da transferência")
    elif tipo == "saque":
        print("Alerta: confirmar com o cliente")
    else:
        print("Transação normal")

analisar_transacao(8000, "transferência")
analisar_transacao(2000, "saque")
analisar_transacao(1000, "pagamento")
