# Lista de strings
frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Imprimindo apenas a frutas "uva"
print(frutas[2])

# Substituindo "pera" por "melão"
frutas[3] = "melão"
print(frutas)

# Descobrindo quantos elementos há na lista
print(len(frutas))

print('----------------------')

# Percorrendo e imprimindo cada um dos elementos da lista
for fruta in frutas:
    print(fruta)

print('----------------------')

# Percorrendo e imprimindo cada elemento e sua posição
for i in range(len(frutas)):
    print(f"{frutas[i]} está na posição {i}")

print('----------------------')

# Percurso em ordem invertida
# 1º argumento: len(frutas) -1: a lista precisa começar no último elemento, que é determinado por len() - 1
# 2º argumento: -1, porque o limite final não entra e precisamos terminar em 0
# 3º argumento: -1, porque a lista precisa ser decrescente
for j in range(len(frutas) -1, -1, -1):
    print(frutas[j])

print('----------------------')

# Ordenando o vetor em ordem alfabética
frutas.sort()
print(frutas)
