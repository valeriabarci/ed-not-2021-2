from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista.to_str())

# Inserção em lista vazia
lista.insert(0, 'Fusca')
print(lista.to_str())

# Inserção no início da lista
lista.insert(0, 'Chevette')
print(lista.to_str())

# Inserção no final da lista
lista.insert(3, 'Maverick')
print(lista.to_str())

# Inserção no final da lista (2)
lista.insert(4, 'Opala')
print(lista.to_str())

# Inserção no final da lista (3)
lista.insert(5, 'Del Rey')
print(lista.to_str())

# Inserção em posição intermediária
lista.insert(1, 'Gol')
print(lista.to_str())

# Inserção em posição intermediária
lista.insert(4, 'Corcel')
print(lista.to_str())

# Remoção do primeiro nodo
removido = lista.remove(0)
print(f"Removido primeira posição: {removido}")
print(lista.to_str())

# Remoção do último nodo
removido = lista.remove(lista.count() - 1)
print(f"Removido última posição: {removido}")
print(lista.to_str())

# Remoção de posição intermediária
removido = lista.remove(2)
print(f"Removido posição 2: {removido}")
print(lista.to_str())

# Consulta o último nodo
ultimo = lista.peek_tail()
print(f"Último nodo consultado: {ultimo}")
print(lista.to_str())

# Inserções adicionais no final da lista
lista.insert_tail('Passat')
lista.insert_tail('Fiorino')
lista.insert_tail('Variant')
lista.insert_tail('Escort')
lista.insert_tail('Del Rey')
print(lista.to_str())

#Testando index
idxCorcel = lista.index('Corcel')
idxVariant = lista.index('Variant')
idxEscort = lista.index('Escort')
idxGol = lista.index('Gol')
idxChevette = lista.index('Chevette')
idxPassat = lista.index('Passat')

print(f"Posições: Corcel: {idxCorcel}, Variant: {idxVariant}, Escort: {idxEscort}, Gol: {idxGol}, Chevette: {idxChevette}, Passat: {idxPassat}")

