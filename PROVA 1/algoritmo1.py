"""
    1) Identifique o algoritmo abaixo.
    # Quick Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def m(n, o = 0, p = None):  # "o" é o início da lista(n), "p" é o fim da lista(n)
    # Erro: é preciso declarar as variáveis de inicio e fim o = 0 e p = None.
    """
        Função que implementa o algoritmo de ordenação
        Quick Sort de forma recursiva
    """
    # Se p for None, então consideramos a última posição do "n"
    if p is None: p = len(n) - 1

    if p <= o: return   # Sai da função sem realizar nada

    q = p           # O "q" é o último elemento, conhecido como pivot
    r = o - 1       # O "r" inicia antes do primeiro elemento
    for i in range(o, p):
        if n[i] < n[q]:
            r += 1      # Incrementa o "r"
            if r != i: n[r], n[i] = n[i], n[r]
    
    # Depois que o percurso de i acaba, o "r" ainda ´é incrementado mais uma vez
    r += 1

    # A troca acontece se o pivot(q) for menor que o valor da posição "r"
    if n[q] < n[r] and q != r: n[q], n[r] = n[r], n[q]

    # Chama-se recursivamente a função para a sublista à esquerda da posição "r"
    m(n, o, r - 1)
    # Chama-se recursivamente a função para a sublista à direita da posição "r"
    m(n, r + 1, p)