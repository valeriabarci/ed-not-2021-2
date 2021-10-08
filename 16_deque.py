from lib.deque import Deque

deque = Deque()     # Cria um deque vazio
print(deque.to_str())

# Inserções "normais"
deque.insert_back("Tertuliano")
deque.insert_back("Castorina")
deque.insert_back("Astolfo")
deque.insert_back("Wesclerson")
deque.insert_back("Gilvanete")

print(deque.to_str())

# Inserções prioritárias
deque.insert_front("Hermógenes")
deque.insert_front("Querência")

print(deque.to_str())

# Remoções "normais"
atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

atendido = deque.remove_front()
print(f"Atendido: {atendido}")
print(deque.to_str())

# Desistências (remoção no final)
desistente = deque.remove_back()
print(f"Desistente: {desistente}")
print(deque.to_str())

desistente = deque.remove_back()
print(f"Desistente: {desistente}")
print(deque.to_str())

# Consultando as extremidades do deque
primeiro = deque.peek_front()
ultimo = deque.peek_back()
print(f"Primeiro : {primeiro}, Último: {ultimo}")
print(deque.to_str())