produtos_a = ['banana', 'maçã']
produtos_b = ['laranja', 'pera']
produtos_c = ['laranja', 'banana', 'maçã', 'romã']


def unificar_estoque(lista1, lista2, lista3):
    estoque_total = lista1 + lista2 + lista3
    print('Estoque total: ', estoque_total)

    for produto in set(estoque_total):
       print(f"{produto}: {estoque_total.count(produto)} unidade(s)")

print(unificar_estoque(produtos_a, produtos_b, produtos_c)
      )
