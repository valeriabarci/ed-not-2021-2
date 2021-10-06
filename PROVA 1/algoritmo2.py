"""
    1) Identifique o algoritmo abaixo.
    # Busca Binária
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

def m(n, o):        # "n" é a lista e o "o" é a busca
    """
        Função que implementa o algoritmo de busca binária
        Retorna a posição onde o "o" foi encontrado ou o valor
        convencional -1 se "o" não existir no "n"
    """
    p = 0           # Primeira posição         
    q = len(n) - 1  # Última posição 
    while p <= q:       # "p" = inicio, "q" = fim
        r = (p + q) // 2     # Erro: Para realizar a divisão inteira é necessário colocar 2 barras (//)
                            # Erro: Deve ser declarado o inicio e o fim

        # 1º caso: n[r] é igual o "o"
        if n[r] == o:
            return r     # r é a posição onde a variável "o" está em "n"

        # 2º caso: "o" é menor que n[r]
        elif o < n[r]: 
            q = r - 1

        # 3º caso: "o" é maior que n[r]
        else:
            p = r + 1

        # 4º caso: "o" não encontrado em "n"
    return -1