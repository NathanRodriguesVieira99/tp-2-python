# Cenário A
pedidos = ['P123', 'P456', 'P789']
pedido_a_substituir = 'P456'
prioridade_urgente = True
pedido_urgente = 'P999'


if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
print('Fila final (Cenário A): ', pedidos)


# Cenário B
pedidos = ['P123', 'P456', 'P789']
pedido_a_substituir = 'P456'
prioridade_urgente = False
pedido_urgente = 'P999'

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        index = pedidos.index(pedido_a_substituir)
        pedidos[index] = pedido_urgente
print('Fila final (Cenário B): ', pedidos)


# Cenário C
pedidos = ['P123', 'P888', 'P789']
pedido_a_substituir = 'P456'
prioridade_urgente = False
pedido_urgente = 'P999'

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        index = pedidos.index(pedido_a_substituir)
        pedidos[index] = pedido_urgente
    else:
        print('Pedido a substituir não está na lista. Nenhuma alteração feita.')
print('Fila final (Cenário C):', pedidos)
