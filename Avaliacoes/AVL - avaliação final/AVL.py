from No import No

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
            
    def _rotacao_direita(self, pai): #fator < -1/
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

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            
        else:
            print(f"-----Inserindo Nó folha: {valor}-----")
            self.raiz = self._inserir_no_folha(self.raiz, valor)

    def _inserir_no_folha(self, no_atual, valor):
        if not no_atual:
            return No(valor)
        elif valor < no_atual:
            no_atual.esquerda = self._inserir_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._inserir_no_folha(no_atual.direita, valor)

        #calcular a altura
        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))

        fator = self._get_fator_balanceamento(no_atual)

        if fator < -1:
            if valor < no_atual.esquerda.valor: #rotação simples para a direita
                self._rotacao_direita(no_atual)
            else: #rotação dupla 1) esquerda 2)direita
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                self._rotacao_direita(no_atual)   
                
        elif fator > 1:
            if valor < no_atual.direita.valor: #rotação simples para a esquerda
                self._rotacao_esquerda(no_atual)
            else: #rotação dupla 1)direita 2)esquerda
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                self._rotacao_esquerda(no_atual)
        return no_atual