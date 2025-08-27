data_atual = '2025-08-12'
boletos = [
    ["B001", 500.00, "2025-08-05"],
    ["B002", 320.00, "2025-08-12"],
    ["B003", 150.00, "2025-08-15"],
    ["B004", 980.00, "2025-08-01"]
]


juros_diario = 0.02

total_devido = 0.0
for boleto in boletos:
    codigo, valor, vencimento = boleto
    if vencimento < data_atual:
        
        from datetime import date
        ano_v, mes_v, dia_v = map(int, vencimento.split("-"))
        ano_a, mes_a, dia_a = map(int, data_atual.split("-"))
        dias_atraso = (date(ano_a, mes_a, dia_a) -
                       date(ano_v, mes_v, dia_v)).days
        valor_devido = valor + (valor * juros_diario * dias_atraso)
        total_devido += valor_devido
        
        print(f"Boleto: {codigo} | Vencimento: {vencimento} | Valor Original: R$ {valor:.2f} | Dias em atraso: {dias_atraso} | Valor Devido: R$ {valor_devido:.2f}")
        
print(f"\nTotal acumulado dos boletos vencidos: R$ {total_devido:.2f}")
