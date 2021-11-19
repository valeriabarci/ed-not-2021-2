from lib.binary_search_tree import BinarySearchTree

arvore = BinarySearchTree()

arvore.insert(48)
arvore.insert(15)
arvore.insert(71)
arvore.insert(1)
arvore.insert(29)
arvore.insert(57)
arvore.insert(80)
arvore.insert(13)
arvore.insert(19)
arvore.insert(37)
arvore.insert(51)
arvore.insert(64)
arvore.insert(23)
arvore.insert(21)
arvore.insert(25)

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

# Teste de exclusão

em_ordem = []
arvore.in_order_traversal(lambda val: em_ordem.append(val))
print('Antes da exclusão do 29 (grau 2): ', em_ordem)

arvore.remove(29)

em_ordem = []
arvore.in_order_traversal(lambda val: em_ordem.append(val))
print('Depois da exclusão do 29 (grau 2): ', em_ordem)

arvore.remove(21)

em_ordem = []
arvore.in_order_traversal(lambda val: em_ordem.append(val))
print('Depois da exclusão do 21 (grau 0): ', em_ordem)

arvore.remove(1)

em_ordem = []
arvore.in_order_traversal(lambda val: em_ordem.append(val))
print('Depois da exclusão do 1 (grau 1): ', em_ordem)

arvore.remove(48)

em_ordem = []
arvore.in_order_traversal(lambda val: em_ordem.append(val))
print('Depois da exclusão do 48 (grau 2, raiz): ', em_ordem)

# Observando qual valor se tornou a nova raiz
# Fazendo um percurso pré-ordem e verificando o primeiro valor retornado
pre_ordem = []
arvore.pre_order_traversal(lambda val: pre_ordem.append(val))
print('Novo nodo raiz tem o valor ', pre_ordem[0])