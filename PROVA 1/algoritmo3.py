"""
    1) Identifique o algoritmo abaixo.
    # Bubble Sort
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""
def m(n):
    """
        Função que implementa o algoritmo de ordenação Bubble Sort
    """

    while 1 > 0:    # Loop infinito
        o = False   # "o" se houve a troca
        # Loop na lista até o PENÚLTIMO elemento: len(o) - 2 -> range(len(o)-1)
        # A última posição estará em len(o) -1
        for p in range(len(n) - 1): # Erro: Deve ser colocado o "n" em vez do "o" dentro do len para iniciar uma nova passada
            if n[p + 1] < n[p]:     # É necessário realizar a troca
                n[p + 1], n[p] = n[p], n[p + 1]     # Realiza a troca
                o = True
        
        # Se houver troca, a lista está ordenada e podemos interromper o loop while
        if not o:       # o == False
            break       # Interrompe o while