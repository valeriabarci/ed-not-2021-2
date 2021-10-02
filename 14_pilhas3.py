"""
    ANALISADOR DE EXPRESSÕES MATEMÁTICAS
"""
from lib.stack import Stack

simbolos = {
    "P": "parêntese",
    "C": "colchete",
    "X": "chave"
}

expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1] * 3} / 5"
#expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1} * 3] / 5"
#expressao = "2 * 4 - {7 / [5 - (7 * 9) + 1]] * 3} / 5"
#expressao = "2 * {4 - {7 / [(5 - (7 * 9) + 1] * 3} / 5"

analisador = Stack()    # Cria a pilha

def verif_fechamento(tipo_fecha, pos_fecha, dados_abre):
    # Se o tipo que veio da pilha for igual ao tipo encontrado
    # no fechamento, OK
    #print(f"DEBUG -> tipo_fecha: {tipo_fecha}, pos_fecha: {pos_fecha}, dados_abre: {dados_abre}")
    
    # A pilha ficou vazia antes do término da análise da expressão
    if dados_abre is None:
        print(f"ERRO: há mais símbolos de fechamento que símbolos de abertura na expressão; tipo {tipo_fecha}, posição {pos_fecha}")
    elif dados_abre["tipo"] == tipo_fecha:
        print(f"Símbolo tipo {tipo_fecha} aberto na posição {dados_abre['pos']} e fechado na posição {pos_fecha}")
    else: # Tipos errados
        print(f"ERRO: símbolo de fechamento do tipo {tipo_fecha} encontrado na posição {pos_fecha}; esperado símbolo do tipo {dados_abre['tipo']}")

# Percorre a expressao em busca de parênteses, colchetes e chaves
for pos in range(len(expressao)):
    if expressao[pos] == "(":
        # Empilha informações sobre o abre parênteses
        analisador.push({ "tipo": "P", "pos": pos})
    elif expressao[pos] == "[":
        #Empilha informações sobre o abre colchetes
        analisador.push({ "tipo": "C", "pos": pos})
    elif expressao[pos] == "{":
        # Empilha informações sobre o abre chaves
        analisador.push({ "tipo": "X", "pos": pos})
    elif expressao[pos] == ")":
        verif_fechamento("P", pos, analisador.pop())
    elif expressao[pos] == "]":
        verif_fechamento("C", pos, analisador.pop())
    elif expressao[pos] == "}":
        verif_fechamento("X", pos, analisador.pop())

# Verificando se houve sobra(s) na pilha
while not analisador.is_empty():
    sobra = analisador.pop()
    print(f"ERRO: símbolo de abertura {sobra['tipo']} sem símbolo de fechamento correspondente na posição {sobra['pos']}")

