from lib.queue import Queue

fila = Queue()      # Cria uma nova fila
print(fila.to_str())

# Adicionando pessoas à fila
fila.enqueue("Marciovaldo")
fila.enqueue("Gildanete")
fila.enqueue("Terencionildo")
fila.enqueue("Junislerton")
fila.enqueue("Ritielaine")

print(fila.to_str())

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila.to_str())

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila.to_str())

fila.enqueue("Adenoirton")
print(fila.to_str())

proximo = fila.peek()
print(f"Próximo a ser atendido: {proximo}")
print(fila.to_str())