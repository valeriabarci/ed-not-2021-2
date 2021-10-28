"""
    Classe que representa cada unidade (elemento) da lista encadeada
    É dividida em três partes:
    1) O ponteiro para o nodo anterior da sequência (prev)
    2) Onde fica armezenada a informação relevante para o usuário (data)
    3) O ponteiro para o próximo nodo da sequência (next)
"""

import math

class Node:
    def __init__(self, val):
        self.prev = None    # Ponteiro para o nodo anterior (None = nenhum)
        self.data = val     # Armazena a informação do usuário
        self.next = None    # Ponteiro para o próximo nodo (None = nenhum)

"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    - A lista encadeada é uma estrutura de dados formada por unidades
      de informação chamadas nodos ou nós.
    - Cada nodo da lista encadeada tem três partes: uma, que armazena a
      informação; a segunda, que guarda o endereço do nodo anterior; e a
      terceira, que guarda o endereço para o nodo seguinte da sequência
    - A qualquer momento, temos um conhecimento apenas limitado de onde
      se encontram todos os nodos da lista. Sabemos apenas onde está o
      primeiro e o último nodo da sequência. Os nodos intermediários precisam
      ser encontrados partindo-se do primeiro OU do último nodo e percorrendo
      a sequência
"""
class DoublyLinkedList:

    """
        Construtor da classe
    """
    def __init__(self):
        self.__head = None  # (cabeça) Aponta para o início da lista
        self.__tail = None  # (cauda) Aponta para o fim da lista
        self.__count = 0    # Contador de nodos

    """
        Método que informa se a lista está ou não vazia
    """
    def is_empty(self):
        return self.__count == 0

    """
        Método que retorna o número de nodos da lista
    """
    def count(self):
        return self.__count

    """
        Método PRIVADO que encontra um nodo, dada a sua posição
    """
    def __find_node(self, pos):
        # Encontra o nodo fazendo o percurso a partir de __head,
        # se ele estiver na primeira metada da lista
        if pos < self.__count // 2:
            node = self.__head
            for i in range(1, pos + 1): node = node.next

        # Se, ao contrário, o nodo estiver na segunda metade da
        # lista, compensa mais fazer um percurso reverso desde
        # o __tail
        else:
            node = self.__tail
            for i in range(self.__count - 2, pos - 1, -1): node = node.prev

        return node

    """
        Método que encontra a posição de um nodo, dado o seu valor
    """
    def index(self, val):
        # Encontra a posição do meio da lista. Se o resultado for
        # fracionário, considera o próximo número inteiro
        meio = math.ceil(self.count / 2)

        # Inicializa dois nodos, um com a cabeça e outro com a cauda
        # da lista
        node1 = self.__head
        node2 = self.__tail

        # Contador que vai até a metade da lista
        for pos in range(0, meio + 1):
            if(node1.data == val): return pos # retorna a posição encontrada
            if(node2.data == val): return self.__count - 1 - pos  # retorna posição retroativa
            node1 = node1.next  # node1 anda para frente
            node2 = node2.prev  # node2 anda para trás

        return -1   # Não encontrou o valor na lista
    
    """
        Método para inserção de um novo nodo na lista
    """
    def insert(self, pos, val):

        inserted = Node(val)

        # 1º caso: lista vazia
        # O nodo criado será, ao mesmo tempo, o primeiro e o último
        if self.is_empty():
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção na posição inicial
        elif pos == 0:
            inserted.next = self.__head     # Aponta para o seguinte
            self.__head.prev = inserted     # Aponta para o anterior
            self.__head = inserted          # Ajusta o início da lista

        # 3º caso: inserção na posição final
        elif pos >= self.__count:
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediaria
        else:
            node_pos = self.__find_node(pos)
            before = node_pos.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = node_pos
            node_pos.prev = inserted

        self.__count += 1

    """
        Método de atalho para inserção no início da lista
    """
    def insert_head(self, val):
        self.insert(0, val)

    """
        Método de atalho para inserção no final da lista
    """
    def insert_tail(self, val):
        self.insert(self.__count, val)

    """
        Método para remoção em qualquer posição
    """
    def remove(self, pos):

        # 1º caso: lista vazia ou posição fora dos limites
        if self.is_empty() or pos < 0 or pos > self.__count - 1: return None

        # 2º caso: remoção do início da lista
        if pos == 0:
            # Será removido o __head da lista
            removed = self.__head
            # O novo __head passa a ser o nodo seguinte ao removido
            self.__head = removed.next
            # Se __head for um nodo válido, ele não pode ter antecessor (prev)
            if self.__head is not None: self.__head.prev = None
            # Em caso de remoção do único nodo restante, __head é None,
            # e __tail precisa ser None também
            if self.__count == 1: self.__tail = None

        # 3º caso: remoção do último nodo
        elif pos == self.__count - 1:
            # Será removido o __tail da lista
            removed = self.__tail
            # O novo __tail passa ser o nodo anterior ao removido
            self.__tail = removed.prev
            # Se __tail for um nodo válido, ele não pode ter sucessor (next)
            if self.__tail is not None: self.__tail.next = None
            # Em caso de remoção do único nodo restante, __tail é None,
            # e __head precisa ser None também
            if self.__count == 1: self.__head = None
            
        # 4º caso: remoção de posição intermediária
        else:
            # Manda encontrar o nodo a ser removido
            removed = self.__find_node(pos)
            before = removed.prev   # Nodo anterior ao removido
            after = removed.next    # Nodo posterior ao removido
            # O nodo before passa a apontar à frente para o nodo after
            before.next = after
            # O nodo after passa a apontar para trás para o nodo before
            after.prev = before

        self.__count -= 1

        return removed.data

    """
        Método de atalho para remoção na primeira posição
    """
    def remove_head(self):
        return self.remove(0)

    """
        Método de atalho para remoção na última posição
    """
    def remove_tail(self):
        return self.remove(self.__count - 1)

    """
        Método para consultar qualquer nodo, dada a sua posição
    """
    def peek(self, pos):

        # Lista vazia ou posição fora dos limites
        if self.is_empty() or pos < 0 or pos > self.__count - 1: return None

        node = self.__find_node(pos)

        return node.data

    """
        Método de atalho para consultar o primeiro nodo
    """
    def peek_head(self):
        return self.peek(0)

    """
        Método de atalho para consultar o último nodo
    """
    def peek_tail(self):
        return self.peek(self.__count - 1)
            
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

#######################################################

lista = DoublyLinkedList()
print(lista.to_str())

# Inserção em lista vazia
lista.insert(0, 'Fusca')
print(lista.to_str())

# Inserção no início da lista
lista.insert(0, 'Chevette')
print(lista.to_str())

# Inserção no final da lista
lista.insert(3, 'Maverick')
print(lista.to_str())

# Inserção no final da lista (2)
lista.insert(4, 'Opala')
print(lista.to_str())

# Inserção no final da lista (3)
lista.insert(5, 'Del Rey')
print(lista.to_str())

# Inserção em posição intermediária
lista.insert(1, 'Gol')
print(lista.to_str())

# Inserção em posição intermediária
lista.insert(4, 'Corcel')
print(lista.to_str())

# Remoção do primeiro nodo
removido = lista.remove(0)
print(f"Removido primeira posição: {removido}")
print(lista.to_str())

# Remoção do último nodo
removido = lista.remove(lista.count() - 1)
print(f"Removido última posição: {removido}")
print(lista.to_str())

# Remoção de posição intermediária
removido = lista.remove(2)
print(f"Removido posição 2: {removido}")
print(lista.to_str())

# Consulta o último nodo
ultimo = lista.peek_tail()
print(f"Último nodo consultado: {ultimo}")
print(lista.to_str())