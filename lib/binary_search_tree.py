"""
    Classe que representa cada unidade (elemento) da árvore binária de busca
    É dividida em três partes:
    1) Onde fica armezenada a informação relevante para o usuário (data)
    2) O ponteiro para a subárvore esquerda (left)
    3) O ponteiro para a subárvore direita (right)
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

"""
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    - Árvore ~> é uma estrutura de dados não-linear, hierárquica,
      que é formada recursivamente por outras subárvores.
    - Árvore binária ~> uma árvore na qual cada nodo tem grau máximo
      igual a 2 (ou seja, cada nodo pode ter, no máximo, dois descendentes
      diretos).
    - Árvore binária de busca ~> é uma árvore binária otimizada para a
      operação de busca binária. Por isso, na inserção, os valores são 
      colocados já em ordem.
"""
class BinarySearchTree:

    """
        Construtor da classe
    """
    def __init__(self):
        self.__root = None      # Raiz da árvore

    """
        Método PÚBLICO de inserção na árvore
    """
    def insert(self, val):

        inserted = Node(val)

        # 1º caso: a árvore está vazia
        if self.__root is None: self.__root = inserted

        # 2º caso: inserção recursiva ~> percorrer a árvore recursivamente
        else: self.__insert_node(inserted, self.__root)

    """
        Método __privado para inserção de um nodo na árvore
    """
    def __insert_node(self, inserted, root):
        # 1º caso: valor do nodo é MENOR que o valor da raiz ~> vai para a ESQUERDA
        if inserted.data < root.data:
            # Se o nodo da esquerda estiver desocupado, faz aí a inserção
            if root.left is None: root.left = inserted
            # Senão, passa a considerar o nodo da esquerda como raiz
            else: self.__insert_node(inserted, root.left)
        
        # 2º caso: valor do nodo é MAIOR que o valor da raiz ~> vai para a DIREITA
        elif inserted.data > root.data:
            # Se o nodo da direita estiver desocupado, faz aí a inserção
            if root.right is None: root.right = inserted
            # Senão, passa a considerar o nodo da direita como raiz
            else: self.__insert_node(inserted, root.right)

        # OBSERVAÇÃO: quando inserted.data == root.data (tentativa de inserção
        # de um valor que já existe na árvore), nada acontece. A tentativa é
        # ignorada.

    """
        Método que exibe a árvore recursivamente
    """
    def to_str(self, root = None):

        if root is None: root = self.__root

        output = ''

        if root is not None:
            output += f'[ROOT data: {root.data}]\n'  # \n = Quebra de linha (enter)

            if root.left is not None:
                output += f'(À esquerda de {root.data}) ' + self.to_str(root.left)

            if root.right is not None:
                output += f'(À direita de {root.data}) ' + self.to_str(root.right)

        return output

    """
        PERCURSOS
    """

    """
        Método que faz o percurso em-ordem (in-order traversal)
        1º: visita em-ordem a subárvore esquerda
        2º: visita a raiz
        3º: visita em-ordem a subárvore direita
        Este percurso é utilizado quando se deseja recuperar os elementos
        da árvore em ordem
    """
    def in_order_traversal(self, fnCallback, root = False):

        if root is False: root = self.__root

        if root is not None:
            self.in_order_traversal(fnCallback, root.left) # 1º
            fnCallback(root.data)   # 2º
            self.in_order_traversal(fnCallback, root.right) # 3º

    """
        Método que faz o percurso pré-ordem (pre-order traversal)
        1º: visita a raiz
        2º: visita pré-ordem a subárvore esquerda
        3º: visita pré-ordem a subárvore direita
        Este percurso é utilizado quando se deseja copiar a árvore,
        preservando sua estrutura
    """
    def pre_order_traversal(self, fnCallback, root = False):

        if root is False: root = self.__root

        if root is not None:
            fnCallback(root.data)   # 1º
            self.pre_order_traversal(fnCallback, root.left) # 2º
            self.pre_order_traversal(fnCallback, root.right) # 3º

    """
        Método que faz o percurso pós-ordem (post-order traversal)
        1º: visita pós-ordem a subárvore esquerda
        2º: visita pós-ordem a subárvore direita
        3º: visita a raiz
        Este percurso é utilizado para sumarizações "bottom-up" (de
        baixo para cima, das folhas em direção à raiz) e também pode
        ser usado no processo de remoção de um nodo da árvore
    """
    def post_order_traversal(self, fnCallback, root = False):

        if root is False: root = self.__root

        if root is not None:
            self.post_order_traversal(fnCallback, root.left) # 1º
            self.post_order_traversal(fnCallback, root.right) # 2º
            fnCallback(root.data)   # 3º

    """
        Método PRIVADO que busca recursivamente por um valor na árvore
        Retorna:
            - o nodo que contém o valor, caso este exista
            - None, se não for encontrado
    """
    def __search_node(self, root, key):

        # 1º caso: árvore vazia
        if root is None: return None

        # 2º caso: o valor de key é MENOR que valor da raiz
        # Continua a busca recursivamente pela subárvore ESQUERDA
        if key < root.data: return self.__search_node(root.left, key)

        # 3º caso: o valor de key é MAIOR que o valor da raiz
        # Continua a busca recursivamente pela subárvore DIREITA
        if key > root.data: return self.__search_node(root.right, key)

        # 4º caso: o valor de key é IGUAL ao valor da raiz
        # ENCONTROU O VALOR; retorna o nodo root
        return root

    """
        Método público que retorna se um valor existe na árvore (True)
        ou não (False)
    """
    def exists(self, val):
        node = self.__search_node(self.__root, val)
        if node is None: return False
        else: return True

    """
        Método PRIVADO para encontrar o nodo de menor valor a partir
        da raiz fornecida
    """
    def __min_node(self, root):
        node = root
        while node is not None and node.left is not None:
            node = node.left
        return node

    """
        Método PRIVADO para encontrar o nodo de maior valor a partir
        da raiz fornecida
    """
    def __max_node(self, root):
        node = root
        while node is not None and node.right is not None:
            node = node.right
        return node

    """
        Método público para remoção de um valor da árvore
    """
    def remove(self, val):
        self.__root = self.__remove_node(self.__root, val)

    """
        Método PRIVADO para remoção de um nodo da árvore
    """
    def __remove_node(self, root, val):

        # 1º caso: árvore vazia
        if root is None: return None

        # 2º caso: o valor a ser removido é MENOR que o valor da raiz
        # Continua procurando pelo nodo a ser removido pelo lado ESQUERDO
        if val < root.data: 
            root.left = self.__remove_node(root.left, val)
            return root

        # 3º caso: o valor a ser removido é MAIOR que o valor da raiz
        # Continua procurando pelo nodo a ser removido pelo lado DIREITO
        if val > root.data:
            root.right = self.__remove_node(root.right, val)
            return root

        # 4º caso: o valor a ser removido é IGUAL ao valor da raiz
        # O nodo a ser removido foi encontrado; agora é necessário
        # determinar o grau do nodo para aplicar o algoritmo de remoção
        # correto para cada grau

        # 4.1: remoção de nodo de grau 0
        if root.left is None and root.right is None:
            root = None
            return root

        # 4.2: remoção de nodo de grau 1 com subárvore à esquerda
        if root.left is not None and root.right is None:
            root = root.left
            return root

        # 4.3: remoção do nodo de grau 1 com subárvore à direita
        if root.left is None and root.right is not None:
            root = root.right
            return root

        # 4.4: remoção do nodo de grau 2


######################################################################

arvore = BinarySearchTree()

arvore.insert(43)
arvore.insert(27)
arvore.insert(64)
arvore.insert(36)
arvore.insert(10)
arvore.insert(0)

print(arvore.to_str())

em_ordem = []

def insere_em_ordem(val):
    em_ordem.append(val)

#arvore.in_order_traversal(insere_em_ordem)
arvore.in_order_traversal(lambda val: em_ordem.append(val))
#arvore.in_order_traversal(lambda val: print(val))

print('Percurso em-ordem:', em_ordem)

sumario = BinarySearchTree()

sumario.insert('2')
sumario.insert('1')
sumario.insert('3')
sumario.insert('1.1')
sumario.insert('3.1')
sumario.insert('2.1')
sumario.insert('2.1.1')

em_ordem = []
sumario.in_order_traversal(lambda val: em_ordem.append(val))
print('Sumário em-ordem:', em_ordem)

pre_ordem = []
sumario.pre_order_traversal(lambda val: pre_ordem.append(val))
print('Sumário pré-ordem:', pre_ordem)

pre_ordem = []
arvore.pre_order_traversal(lambda val: pre_ordem.append(val))
print('Árvore pré-ordem:', pre_ordem)

pos_ordem = []
arvore.post_order_traversal(lambda val: pos_ordem.append(val))
print('Árvore pós-ordem:', pos_ordem)

existe36 = arvore.exists(36)
existe51 = arvore.exists(51)
existe64 = arvore.exists(64)
print(f'36: {existe36}, 51: {existe51}, 64: {existe64}')