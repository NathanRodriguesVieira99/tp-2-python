mensagem_encriptada = "SbwKrQ eh phokRu q MDydvfulsW"

chave = 0
for c in mensagem_encriptada:
    if c == 'D' or c == 'd' or c == 'W':
        chave += 1

mensagem_decodificada = ""
palavra = ""
for i in range(len(mensagem_encriptada)):
    letra = mensagem_encriptada[i]
    if letra != " ":
        palavra += letra
    else:

        if len(palavra) > 3:
            nova_palavra = ""
            for l in palavra:
                if l.isalpha():
                    if l.isupper():
                        nova_letra = chr(
                            (ord(l) - ord('A') - chave) % 26 + ord('A'))
                    else:
                        nova_letra = chr(
                            (ord(l) - ord('a') - chave) % 26 + ord('a'))
                    nova_palavra += nova_letra
                else:
                    nova_palavra += l
            mensagem_decodificada += nova_palavra + " "
        else:
            mensagem_decodificada += palavra + " "
        palavra = ""

if len(palavra) > 3:
    nova_palavra = ""
    for l in palavra:
        if l.isalpha():
            if l.isupper():
                nova_letra = chr((ord(l) - ord('A') - chave) % 26 + ord('A'))
            else:
                nova_letra = chr((ord(l) - ord('a') - chave) % 26 + ord('a'))
            nova_palavra += nova_letra
        else:
            nova_palavra += l
    mensagem_decodificada += nova_palavra
else:
    mensagem_decodificada += palavra

print(mensagem_decodificada)
