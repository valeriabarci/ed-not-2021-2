class Stack:
    """
        ESTRUTURAS DE DADOS PILHA
        - Pilha é uma lista linear de acesso restrito, que permite apenas as operações
        de inserção (push) e retirada (pop), ambas ocorrendo no final da estrutura.
        - Como consequência, a pilha funciona pelo princípio LIFO (Last In, First Out - 
        último a entrar, primeiro a sair).
        - A principal aplicação das pilhas são tarefas que envolvem a inversão de uma
        sequência de dados.
    """

    """
        Construtor da classe
    """
    def __init__(self):
        self.__data = []    # Inicializa uma lista privada vazia

    """
        Método para inserção
        O nome do método de inserção em pilhas é padronizado: push()
    """
    def push(self, val):
        self.__data.append(val)

    """
        Método para retirada
        O nome do método de retirada em pilhas também é padronizado: pop()
    """
    def pop(self):
        if self.is_empty(): return None
        else: return self.__data.pop()

    """
        Método para consultar co topo da pilha(último elemento), sem retirá-lo
        Nome padronizado: peek()
    """
    def peek(self):
        if self.is_empty(): return None
        else: return self.__data[-1]

    """
        Método para verificar se a pilha está vazia ou não
        Retorna True se vazia ou False caso contrário
    """
    def is_empty(self):
        return len(self.__data) == 0

    """
        Método que exibe a pilha como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        for el in self.__data:
            if string != "": string += ", "
            string += str(el)
        return "[ " + string + " ]"

##########################################################################

