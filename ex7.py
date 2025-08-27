tentativas_conexao = [False, False, False, True, True]
tentativas = 0
limite_tentativas = 3

indice = 0
while tentativas < limite_tentativas and indice < len(tentativas_conexao):
    print("Tentando conectar...")
    if tentativas_conexao[indice]:
        print("Conexão realizada com sucesso!")
        break
    tentativas += 1
    indice += 1
else:
    print("Conexão interrompida após limite de tentativas")
