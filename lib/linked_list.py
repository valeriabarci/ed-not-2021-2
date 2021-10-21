"""
    Classe que representa cada unidade (elemento) da lista encadeada
    É divido em duas partes:
    1) Onde fica armazenada a informação relevante para o usuário (__data)
    2) O ponteiro para o próximo nodo da sequência (next)
"""
class Node:

    def __init__(self, val):
        self.data = val     # Armazena a informação do usuário
        self.next = None    # Ponteiro para o próximo nodo (None = nenhum)

"""
    ESTRUTURA DE DADOS LISTA ENCADEADA
    - A lista encadeada é uma estrutura de dados formada por unidades
    de informação chamadas nodos ou nós.
    - Cada nodo da lista encadeada tem duas partes: uma, que armazena a 
    informação e outra que guarda o endereço do próximo nodo da sequência.
    - A qualquer momento, temos um conhecimento apenas limitado de onde
    se encontram todos os nodos da lista. Sabemos apenas onde está o
    primeiro e o último nodo da sequência. Os nodos intermediários precisam
    ser encontrados partindo-se do primeiro e percorrendo a sequência.
"""
class LinkedList:

    """
        Construtor da classe
    """
    def __init__(self):
        self.__head = None      # (head = cabeça (da lista)) Ponteiro para o primeiro nodo da lista
        self.__tail = None      # (tail = calda) Ponteiro para o último nodo da lista
        self.__count = 0        # Contador de nodos

    """
        Método que informa se a lista está ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    def insert(self, pos, val):

        inserted = Node(val)

        # 1º caso: a lista está vazia
        # O nodo criado será, ao mesmo tempo, o primeiro e o último
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted
        
        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head = inserted

        # 3º caso: inserção no fim da lista
        # Vamos considerar qualquer posição de inserção >= count
        # como inserção no final
        elif pos >= self.__count:
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        else:
            before = self.__head

        # Percorre a lista encadeada da segunda podição (pos. 1)
        # até a posição ANTERIOR aquela de inserção
            for i in range(1, pos): before = before.next

            # Nodo que ficará DEPOIS do inserido
            after = before.next
        
            # O next do nodo inserido passa a ser o after
            inserted.next = after

            # O next do nodo before passa a ser o inserted
            before.next = inserted

        self.__count += 1
    
    """
        Método de atalho para inserção na primera posição
    """
    def insertFront(self, val):
        self.insert(0, val)

    """
        Método de atalho para inserção na última posição
    """
    def insertBack(self, val):
        self.insert(self.__count, val)
    
    """
        Retorna o campo data do nodo da posição especificada
    """
    def peek(self, pos):
        # Quando a lista estiver vazia ou a posição estiver fora
        # dos limites válidos (0..count - 1), retorna None
        if self.is_empty() or pos < 0 or pos > self.__count - 1:
            return None
        node = self.__head
        for i in range(0, pos): node = node.next
        return node.data

    """
        Método para procurar um valor na lista e retornar sua posição.
        Retorna - 1 caso não encontre.
    """
    def index(self, val):
        node = self.__head
        for pos in range(0, self.__count):
            if node.data == val: return pos
            node = node.next
        return -1   # Não encontrou

    """
        Método para remover um elemento da lista
    """
    def remove(self, pos):
        
        # 1º caso: lista vazia ou posição fora dos limites
        # (menor que 0 ou maior que count -1)
        if self.__count == 0 or pos < 0 or pos > self.__count - 1:
            return None

        # 2º caso: remoção do início da lista
        if pos == 0:
            removed = self.__head           # Nodo removido
            self.__head = self.__head.next  # Passa a apontar para o nodo seguinte

        # 3º caso: remoções intermediárias ou finais
        else:
            # Percorre a lista até encontrar o item anterior
            # à posição de remoção (before)
            before = self.__head
            for i in range(1, pos): before = before.next

            # O removido será o sucessor do before
            removed = before.next

            # Nodo da posição seguinte à de remoção (next)
            after = removed.next

            # O nodo anterior (before) passa a apontar para o
            # nodo seguinte (after)
            before.next = after

            # Atualizando o __tail no caso da remoção do último nodo
            if removed == self.__tail:
                self.__tail = before
                # print(f"Valor do _tail: {self.__tail.data}")

        self.__count -= 1
        # Retorna o valor armazenado no nodo removido
        return removed.data

    """
        Método para remover o primeiro nodo da lista
    """
    def removeHead(self):
        return self.remove(0)

    """
        Método para remover o último nodo da lista
    """
    def removeTail(self):
        return self.remove(self.__count - 1)

    """
        Método que retorna a quantidade de itens da lista
    """
    def count(self):
        return self.__count

    """
        Método que exibe a lista como uma string (para fins de depuração)
    """
    def to_str(self):
        string = ""
        node = self.__head
        for i in range(0, self.__count):
            if string != "": string += ", "
            string += f"(pos: {i}, data: {node.data})"
            node = node.next
        return "[ " + string + f" ], count: {self.__count}"

######################################################################