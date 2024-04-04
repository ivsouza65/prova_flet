"""# Criando a lista de compras com os itens desejados
lista_compras = ["arroz", "feijão", "quiabo"]

# Removendo o último item da lista (quiabo)
lista_compras.pop()

# Adicionando um novo item à lista (batata)
lista_compras.append("batata")

# Encontrando o índice do elemento "feijão" na lista
indice_feijao = lista_compras.index("feijão")

# Contando quantas vezes o elemento "feijão" aparece na lista
quantidade_feijao = lista_compras.count("feijão")

# Ordenando a lista em ordem alfabética
lista_compras.sort()

# Invertendo a ordem da lista
lista_compras.reverse()

# Imprimindo a lista final
print(lista_compras)"""

def lista_operacoes(lista):
  """
  Realiza operações em uma lista.

  Args:
      lista: A lista original para manipulação.

  Returns:
      A lista modificada após as operações.
  """

  # Removendo o último item
  lista.pop()
  print(f"Lista após remover o último item: {lista}")

  # Adicionando um novo item
  lista.append("batata")
  print(f"Lista após adicionar um novo item: {lista}")

  # Encontrando o índice de um item
  indice_feijao = lista.index("feijão")
  print(f"Índice do elemento 'feijão': {indice_feijao}")

  # Ordenando a lista
  lista.sort()
  print(f"Lista ordenada alfabeticamente: {lista}")

  return lista

# Exemplo de uso
lista_compras = ["arroz", "feijão", "quiabo", "quiabo", "feijão"]
lista_final = lista_operacoes(lista_compras.copy())  # Cria cópia para não alterar original
print(f"Lista final: {lista_final}")