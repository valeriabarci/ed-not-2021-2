"""
    Classe que representa cada unidade (elemento) da árvore binária de busca
    É dividida em três partes:
    1) Onde fica armazenada a informação relevante para o usuário (data)
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
        
        # Exibe a árvore (tosco, para debug)
        print(f'[ÁRVORE] data: {self.__root.data}, left: {self.__root.left}, right: {self.__root.right}')
        
    """
        Método privado para inserção de um nodo na árvore
    """
    def __insert_node(self, node, root):
        # 1º caso: valor do nodo é MENOR que o valor a raiz ~> vai para a ESQUERDA
        if node.data < root.data:
            # Se o nodo da esquerda estiver desocupado, faz aí a inserção
            if root.left is None: root.left = node
        # 2º caso: valor do nodo é MAIOR que o valor da raiz ~> vai para a DIREITA
        elif node.data > root.data:
            # Se o nodo da direita estiver desocupado, faz aí a inserção
            if root.right is None: root.right = node
            
####################################################################################

arvore = BinarySearchTree()

arvore.insert(43)
arvore.insert(27)
arvore.insert(64)
