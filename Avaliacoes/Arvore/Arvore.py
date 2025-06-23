from No import No

class Arvore:
    def __init__(self):
        self.raiz = None

    def adicionar(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._adicionar_recursivo(self.raiz, valor)
                                    # nodo_atual, valor

    def _adicionar_recursivo(self, nodo_atual, valor):
        if valor < nodo_atual.valor: #verificar se o nodo atual é maior que o valor do parametro
            if nodo_atual.esquerda is None:
                nodo_atual.esquerda = No(valor)
            else:
                self._adicionar_recursivo(nodo_atual.esquerda, valor)
        
        else:
            if nodo_atual.direita is None:
                if nodo_atual.direita is None:
                    nodo_atual.direita = No(valor)

                else:
                    self._adicionar_recursivo(nodo_atual.direita, valor)


    def imprimir(self):
        if self.raiz is None:
            print("Árvore vazia!!!")
        else:
            self._imprimir_recursivo(self.raiz)
        print("-" * 20)

    
    def _imprimir_recursivo(self, nodo_atual):
        if nodo_atual






arvore_binaria = Arvore()
arvore_binaria.adicionar(30)
arvore_binaria.adicionar(32)
arvore_binaria.adicionar(20)