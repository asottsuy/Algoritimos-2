from ArvoreGenerica import ArvoreGenerica

arvore = ArvoreGenerica()

def adicionarRamo(arvore):
    while True:
        arvore.imprimir()
        print("\nEntre com os dados: ")
        valor = input("Digite o valor/dado a ser inserido: ")
        if not valor:
            break
    

        pai = None
        if not arvore.vazia():
            pai = input("Digite o pai para esse dado inserido: ")
            if not pai:
                break
        
            arvore.adicionar_valor(valor, pai)
            

adicionarRamo(arvore)