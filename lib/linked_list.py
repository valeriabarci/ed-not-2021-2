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

lista = LinkedList()

lista.insert(0, "1 kg batata")
lista.insert(1, "café")
lista.insert(2, "miojo")
lista.insert(3, "óleo")
lista.insert(4, "sabonete")
lista.insert(5, "shampoo")

lista.insert(4, "tomate")

lista.insert(7, "sabão em pó")
lista.insert(30, "detergente")

#print(lista.to_str())

lista.insertFront("5 kg arroz")
lista.insertBack("água sanitária")

print(lista.to_str())

print(f"Info do nodo da posição 7:  {lista.peek(7)}")
print(f"Info do nodo da posição 13:  {lista.peek(13)}")

print(f"Posição de tomate: {lista.index('tomate')}")
print(f"Posição de café: {lista.index('café')}")
print(f"Posição de cebola: {lista.index('cebola')}")