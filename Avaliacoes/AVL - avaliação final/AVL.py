from turtle import filling


class AVL:
    def __init__(self):
        self.raiz = None
    
    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def _get_fator_balanceamento(self, nodo):
        if not nodo:
            return 0
        # Fator = Altura da Direita - Altura da Esquerda
        return self._get_altura(nodo.direita) - self._get_altura(nodo.esquerda)
            
    def _rotacao_direita(self, pai): #fator < -1
        filhoE = pai.esquerda
        neto = filhoE.direita
        filhoE.direita = pai
        pai.esquerda = neto

        pai.altura = 1 + max(self._get_altura(pai.esquerda), self._get_altura(pai.direita))

        filhoE = 1 + max(self._get_altura(filhoE.esquerda), self._get_altura(filhoE.direita))

        return filhoE
    
    def _rotacao_esquerda(self, pai): #fator > 1
        filhoD = pai.direita
        neto = filhoD.esquerda
        filhoD.esquerda = pai
        pai.direita = neto

        pai.altura = 1 + max(self._get_altura(pai.esquerda), self._get_altura(pai.direita))

        filhoD = 1 + max(self._get_altura(filhoD.esquerda), self._get_altura(filhoD.direita))

        return filhoD
