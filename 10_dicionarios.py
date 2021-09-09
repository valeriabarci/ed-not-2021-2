# Dicionário é uma estrutura de linguagem Python
# capaz de armazenar múltiplos valores em uma única
# variável, por meio de pares de chave-valor
pessoa = {
    # "nome" é a chave
    # "Fulano de Tal" é o valor
    "nome": "Fulano de Tal",
    "sexo": "M",
    "idade": 39,
    "peso": 76,
    "altura": 1.82
}

# Calculando o IMC (Indice de Massa Corporal)
imc = pessoa["peso"] / (pessoa["altura"] ** 2)
print(f"O IMC de {pessoa['nome']} é {imc}.")
print(pessoa)

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"     # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse
}
forma4 = {
    "base": 10,
    "altura": 5,
    "tipo": "W"     # Tipo não reconhecido
}

forma5 = {
    "legume": "batata",
    "fruta": "abacate",
    "tipo": "T"
}

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":    # Retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":  # Triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":  # Elipse
        return forma["base"] / 2 * forma["altura"] / 2 * pi
    else:
        # Gera um erro
        raise Exception("Tipo de forma não reconhecido.")
print(f"Área de um retângulo de 7.5x12: {calcular_area(forma1)}")
print(f"Área de um triângulo de 6x2.5: {calcular_area(forma2)}")
print(f"Área de uma elipse de 5x3: {calcular_area(forma3)}")
#print(f"Área de uma forma desconhecida de 10x5: {calcular_area(forma4)}")
print(f"Área de uma forma desconhecida de ?x?: {calcular_area(forma5)}")




