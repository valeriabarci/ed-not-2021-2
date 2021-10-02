from lib.stack import Stack

# Criando uma pilha
pilha = Stack()
print(pilha.to_str())

# Empilhando valores
pilha.push(10)
pilha.push(13)
pilha.push(19)
pilha.push(23)
pilha.push(27)
pilha.push(33)

print(pilha.to_str())

# Retirar um elemento da pilha
removido = pilha.pop()
print(f"Removido: {removido}, pilha: {pilha.to_str()}")

# Consultar o último elemento
ultimo = pilha.peek()
print(f"Último: {ultimo}, pilha: {pilha.to_str()}")

# Esvaziar a pilha, elemento por elemento
while not pilha.is_empty():
    print(pilha.pop())

print(pilha.to_str())

# Retirar um elemento da pilha (vazia)
removido = pilha.pop()
print(f"Removido: {removido}, pilha: {pilha.to_str()}")

# Consultar o último elemento (vazia)
ultimo = pilha.peek()
print(f"Último: {ultimo}, pilha: {pilha.to_str()}")