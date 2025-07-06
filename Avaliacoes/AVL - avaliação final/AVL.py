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

        filhoE.altura = 1 + max(self._get_altura(filhoE.esquerda), self._get_altura(filhoE.direita))

        return filhoE
    
    def _rotacao_esquerda(self, pai): #fator > 1
        filhoD = pai.direita
        neto = filhoD.esquerda
        filhoD.esquerda = pai
        pai.direita = neto

        pai.altura = 1 + max(self._get_altura(pai.esquerda), self._get_altura(pai.direita))

        filhoD.altura = 1 + max(self._get_altura(filhoD.esquerda), self._get_altura(filhoD.direita))

        return filhoD

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            
        else:
            print(f"-----Inserindo Nó folha: {valor}-----\n")
            self.raiz = self._inserir_no_folha(self.raiz, valor)

    def _inserir_no_folha(self, no_atual, valor):
        if not no_atual:
            return No(valor)
        elif valor < no_atual.valor:
            no_atual.esquerda = self._inserir_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._inserir_no_folha(no_atual.direita, valor)

        #calcular a altura
        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))

        fator = self._get_fator_balanceamento(no_atual)

        if fator < -1:
            if valor < no_atual.esquerda.valor: #rotação simples para a direita
                return self._rotacao_direita(no_atual)
            else: #rotação dupla 1) esquerda 2)direita
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)   
                
        elif fator > 1:
            if valor > no_atual.direita.valor: #rotação simples para a esquerda
                return self._rotacao_esquerda(no_atual)
            else: #rotação dupla 1)direita 2)esquerda
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                return self._rotacao_esquerda(no_atual)
        return no_atual
    

            # Dentro da classe AVL
    def imprimir_como_diretorio(self):
        """Método público para iniciar a impressão em estilo de diretório."""
        if not self.raiz:
            print("A árvore está vazia.")
        else:
            self._imprimir_como_diretorio_recursivo(self.raiz, "", True)

    def _imprimir_como_diretorio_recursivo(self, no_atual, prefixo, eh_ultimo):
        if no_atual is not None:
            # Imprime o nó atual com o prefixo correto
            print(prefixo + ("└── " if eh_ultimo else "├── ") + f"Valor:{no_atual.valor} (A:{no_atual.altura}) (FB:{self._get_fator_balanceamento(no_atual)})")

            # Prepara o prefixo para os filhos
            prefixo_filho = prefixo + ("    " if eh_ultimo else "│   ")
            
            # Faz uma lista com os filhos do no atual.
            # Ele retira todos os dados NONE
            filhos = [no for no in [no_atual.esquerda, no_atual.direita] if no]
            # retorna o endereço de memoria
            
            #Usamos uma lista para facilitar a iteração e saber quem é o último.
            for i, filho in enumerate(filhos):#enumerate retorna o indice e o filho
                eh_o_ultimo_da_lista = (i == len(filhos) - 1)
                self._imprimir_como_diretorio_recursivo(filho, prefixo_filho, eh_o_ultimo_da_lista)

            '''
            exemplo:    0     1
            filhos = [a310, e550]
            i = 1       filho = 1 
            eh_o_ultimo_da_lista = (1 == 2 - 1) =  True e o ultimo
            recursão novamente

            *dentro do for
                self._imprimir_como_diretorio_recursivo(a310(100), prefixo, eh_o_ultimo_da_lista)
                    print(├── e550, valor)
                    prefixo(└── )

                    filhos = []
                    nem vai iterar -  volta para a o for anterior


            '''

    def excluir (self, valor):
        if self.raiz is None:
            print('Árvore está vazia!')
        else:
            self.raiz = self._excluir_recursivo(self.raiz, valor)

    # Esta função auxiliar vai encontrar o menor nó em uma subárvore
    def _get_no_com_menor_valor(self, no_atual):
        if no_atual is None or no_atual.esquerda is None:
            return no_atual
        return self._get_no_com_menor_valor(no_atual.esquerda)

    def _excluir_recursivo(self, no_atual, valor):
        if not no_atual:
            print(f'Valor: {valor} não encontrado!')
            return no_atual
        elif valor < no_atual.valor: #vai descer pela esquerda
            no_atual.esquerda = self._excluir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._excluir_recursivo(no_atual.direita, valor)

        #se no_atual não atender nenhuma das verificações acima significa q o valor foi encontrado
        else:
            #vamos verificar se o no encontrado tem filhos, pois se tiver precisamos guardar eles para depois fazer as rotações/balanceamento
            if no_atual.esquerda is None:
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                temp = no_atual.esquerda
                no_atual = None
                return temp
            # Encontre o sucessor em ordem (o menor nó na subárvore direita)
            sucessor = self._get_no_com_menor_valor(no_atual.direita)
            no_atual.valor = sucessor.valor
            no_atual.direita = self._excluir_recursivo(no_atual.direita, sucessor.valor)
            
        if no_atual is None:
            return no_atual

        # Fase 2: Rebalanceamento AVL
        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda),
                                  self._get_altura(no_atual.direita))
        fator = self._get_fator_balanceamento(no_atual)

        # Rotações, se necessário
        if fator < -1 and self._get_fator_balanceamento(no_atual.esquerda) <= 0: # Esq-Esq
            return self._rotacao_direita(no_atual)

        if fator < -1 and self._get_fator_balanceamento(no_atual.esquerda) > 0: # Esq-Dir
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        if fator > 1 and self._get_fator_balanceamento(no_atual.direita) >= 0: # Dir-Dir
            return self._rotacao_esquerda(no_atual)

        if fator > 1 and self._get_fator_balanceamento(no_atual.direita) < 0: # Dir-Esq
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
            
        return no_atual


arvore = AVL()
arvore.inserir(100)
arvore.imprimir_como_diretorio()
arvore.inserir(90)
arvore.imprimir_como_diretorio()
arvore.inserir(80)
arvore.imprimir_como_diretorio()
arvore.inserir(110)
arvore.imprimir_como_diretorio()
arvore.inserir(115)
arvore.imprimir_como_diretorio()

arvore.excluir(110)
arvore.imprimir_como_diretorio()
