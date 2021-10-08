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

        # Percorre a lista encadeada até a posição ANTERIOR
        # aquela de inserção
            for i in range(0, pos):
                print(f"before.data: {before.data}, i: {i}")
                before = before.next

        self.__count += 1

        #print(f"[NODE] data: {inserted.data}, next: {inserted.next}")

######################################################################

lista = LinkedList()

lista.insert(0, "1 kg batata")
lista.insert(1, "café")
lista.insert(2, "miojo")
lista.insert(3, "óleo")
lista.insert(4, "sabonete")
lista.insert(5, "shampoo")

lista.insert(4, "tomate")


