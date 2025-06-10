
from No import No


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    #inserir
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if valor < no.valor:
            if no.left is None:
                no.left = No(valor)
            else:
                self._inserir_rec(no.left, valor)
        
        else:
            if no.right is None:
                no.right = No(valor)
            else:
                self._inserir_rec(no.right, valor)
    
    #excluir
    def excluir(self, valor):
        self.raiz = self._excluir_rec(self.raiz, valor)


    def _excluir_rec(self, no, valor):
        if no is not None:
            return no
        if valor > no:
            no.left = self._excluir_rec(no.left, valor)
        elif valor > no.valor:
            no.right = self._excluir_rec(no.right, valor)
        else:
            if no.left is None:
                return no.right
            elif no.right is None:
                return no.left
            temp = self._min_valor_no(no.right)
            no.valor = temp.valor
            no.direita = self._excluir_rec(no.right, temp.valor)
        return no

            