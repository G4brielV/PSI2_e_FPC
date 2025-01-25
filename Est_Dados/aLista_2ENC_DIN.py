class No(): #
    def __init__(self, dado=None):
        self._dado = dado
        self._prox = None
        self._ant = None

    # Getters e Setters

    # Definindo o print do No
    def __str__(self):
        return f"{self._dado}"


class Lista_2ENC():
    # Insere no fim
    # Remove em qualquer lugar

    def __init__(self):
        self._inicio = None
        self._fim = None


    #Lista está vazia?
    def isVazia(self):
        if self._inicio is None:
            return True
        return False

    # Inserir um dado no fim
    def insertLast(self, dado=None):
        novoNo = No(dado)

        # Caso 1: Lista vazia
        if self.isVazia():
            self._inicio = self._fim = novoNo

        #Caso 2: Lista não está vazia
        else:
            novoNo._ant = self._fim
            # novoNo._prox = None --> Não precisa
            self._fim._prox = novoNo
            self._fim = novoNo

    # Busca por dado
    def search(self, dadoProcurado):
        i = self._inicio
        while i is not None:
            # Encontrou a posi do dado
            if dadoProcurado == i._dado:
                return i

            # i recebe o próximo nó
            else:
                i = i._prox

        # Se o item não estiver na lista
        return None

    # Remover um dado em qualquer local da lista
    def delete(self, dadoRemover):
        # Encontrar nó do dado que se deseja remover
        no_dado_remover = self.search(dadoRemover)

        # Verifica se o nó existe:
        if no_dado_remover is not None:
            # Verificando se não tem nó anterior, ou seja, se não é o primeiro da lista
            if no_dado_remover._ant is not None:
                # Transforma o proximo do anterior que será removido no proximo do removido
                no_dado_remover._ant._prox = no_dado_remover._prox
            # Se for o primeiro da lista o inicio deve passar para o próximo
            else:
                self._inicio = no_dado_remover._prox

            # Verificando se não tem um proximo nó, ou seja, se não é o último da lista
            if no_dado_remover._prox is not None:
                # Transforma o anterior do depois que será removido no anterior do removido
                no_dado_remover._prox._ant = no_dado_remover._ant
            # Se for o primeiro da lista o inicio deve passar para o próximo
            else:
                self._fim = no_dado_remover._ant

        return no_dado_remover

    # Definindo o print do da lista
    def __str__(self):
        resp = ""
        i = self._inicio
        while i is not None:
            resp += f" | {str(i)}"
            i = i._prox
        return resp


if __name__ == "__main__":
    # Inserindo dados na lista
    l = [4, 7, 17, 87, 2, 10]
    lista_2_ENC = Lista_2ENC()
    for i in l:
        lista_2_ENC.insertLast(i)

    # Visualizando a lista
    print(f"Lista: {lista_2_ENC}")

    # Procurando itens: 1 que existe na lista e outro que não
    print(f"Pesquisa do item 4 na lista: {lista_2_ENC.search(4)}")
    print(f"Pesquisa do item 90 na lista: {lista_2_ENC.search(90)}")

    # Excluindo itens: 1 que existe na lista e outro que não
    lista_2_ENC.delete(2)
    print(f"Lista - o item 2:  {lista_2_ENC}")
    lista_2_ENC.delete(100) # Não faz nada
    print(f"Lista - o tem 100: {lista_2_ENC}")

    # Excluindo o primeiro:
    lista_2_ENC.delete(4)
    print(f"Lista - o 4 (primeiro item): {lista_2_ENC}")

    # Excluindo o último:
    lista_2_ENC.delete(10)
    print(f"Lista - o 10 (último item): {lista_2_ENC}")
