# Classe é uma estrutura que representa conjuntamente
# dados e algoritmos. Uma classe é como uma "forma de bolo"
# com a qual podemos criar diferentes "bolos" (objetos).
# Cada "bolo" (objeto) pode ser feito com seus próprios
# ingredientes (dados) e modos de fazer (algoritmos), mas
# terão sempre o formato determinado pela "forma" (classe).

class FormaGeometrica():

    # Dados
    # Quando pertence a uma classe, ganham o nome de
    # ATRIBUTOS
    # base = 0
    # altura = 0
    # tipo = "R"  # Retângulo

    # Algoritmos
    # São representados por funções que, quando se encontram
    # dentro de uma classe, ganham o nome de MÉTODOS

    # Este método é executado quando um objeto é criado a partir
    # de uma classe (construtor)
    def __init__(self, base, altura, tipo = "R"):
        # Recebe os valores passados ao construtor e os armazena
        # dentro dos atributos

        #print(f"base: {base} ({type(base)}), altura: {altura} ({type(altura)})")

        if type(base) not in [int, float] or base <= 0:
            raise Exception("A base deve ser numérica e maior que zero.")
        elif type(altura) not in [int, float] or altura <= 0:
            raise Exception("A altura deve ser numérica e maior que zero.")
        elif tipo not in["R", "T", "E"]:
            raise Exception("O tipo deve ser R, T ou E.")


        # Ajustando o valor dos atributos privados
        self.__base = base
        self.__altura = altura
        self.__tipo = tipo

    # Getter é um método que possibilita saber o valor de um atributo
    # privado do lado de fora da classe
    def get_base(self):
        return self.__base

    # Setter é um método que possibilita alterar o valor de um atributo
    # privado inclusive do lado de fora da classe
    def set_base(self, valor):
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception(" * A base deve ser numérica e maior que zero")
        
        self.__base = valor

    # property "esconde" as funções getter e setter dentro do nome de
    # um atributo, tornando mais simples a manipulação do objeto
    base = property(__get_base, __set_base)

    # Essas linhas começadas com @ são chamadas "decorators"
    # Os decorators instruem o Python a criar uma property com
    # um getter e um setter na hora da execução
    @property
    def altura(self):       # Getter para o propriedade chamada "altura"
        return self.__altura

    @altura.setter
    def altura(self, valor):    # Setter para a propriedade chamada "altura"
        if type(valor) not in [int, float] or valor <= 0:
            raise Exception("* A altura deve ser numérica e maior que zero")
        self.__altura = valor

################################################################

# Criando objetos (instanciando) a partir da classe
retangulo1 = FormaGeometrica(15, 10, "R")   # Chama o __init__
triangulo1 = FormaGeometrica(6.4, 9, "T")

#retangulo1.__base = 5
# retangulo1.set_base(9.6)
retangulo1.base = 9.6     # vai executar set_base da classe
#retangulo1.set_base(12.5)

# retangulo1.__base = 0
# triangulo1.__tipo = "Yadayada"

#problematico = FormaGeometrica(7.2, 5.4, "T")

print(f"[retangulo1] base: {retangulo1.base}")  # vai executar o getter

#print(f"[retangulo1] base: {retangulo1.base}, base (de novo): {retangulo1.get_base()}")  # vai executar o getter

#print(f"[retangulo1] base: {retangulo1.__base}, altura: {retangulo1.__altura}, tipo: {retangulo1.__tipo}")

#print(f"[triangulo1] base: {triangulo1.__base}, altura: {triangulo1.__altura}, tipo: {triangulo1.__tipo}")

