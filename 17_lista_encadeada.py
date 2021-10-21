from lib.linked_list import LinkedList

lista = LinkedList()

lista.insert(0, "1 kg batata")
lista.insert(1, "café")
lista.insert(2, "miojo")
lista.insert(3, "óleo")
lista.insert(4, "sabonete")
lista.insert(5, "shampoo")

lista.insert(4, "tomate")

lista.insert(7, "sabão em pó")
lista.insert(30, "detergente")

#print(lista.to_str())

lista.insertFront("5 kg arroz")
lista.insertBack("água sanitária")

print(lista.to_str())

print(f"Info do nodo da posição 7:  {lista.peek(7)}")
print(f"Info do nodo da posição 13:  {lista.peek(13)}")

print(f"Posição de tomate: {lista.index('tomate')}")
print(f"Posição de café: {lista.index('café')}")
print(f"Posição de cebola: {lista.index('cebola')}")

print('--------------------------------')

print(lista.to_str())

# Remoção do início da lista
removido = lista.remove(0)

print(f"Valor removido: {removido}")
print(lista.to_str())

# Remoção na posição 5
removido = lista.remove(5)

print(f"Valor removido da posição 5: {removido}")
print(lista.to_str())

# Remoção do último nodo
removido = lista.remove(lista.count() - 1)

print(f"Valor removido do último nodo: {removido}")
print(lista.to_str())

# Remoção do último nodo (usando removeTail())
removido = lista.removeTail()

print(f"Valor removido do último nodo: {removido}")
print(lista.to_str())