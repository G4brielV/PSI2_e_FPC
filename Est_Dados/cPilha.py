from Est_Dados.aLista_2ENC_DIN import Lista_2ENC, No


class Pilha(Lista_2ENC):
    # Inserir no Inicio
    # Remover no Inicio

    #   insertFirst
    def push(self, dado=None):
        novoNo = No(dado)
        # 1 Caso: Se estiver vazia
        #   - O novo nó é o inicio
        if self.isVazia():
            self._inicio = novoNo

        # 2 Caso: Se não estiver vazia
        #   - Proximo do novo nó é o inicio
        #   - O anterior do incio agr é o novo nó
        #   - O novo nó é o inicio
        else:
            novoNo._prox = self._inicio
            self._inicio._ant = novoNo
            self._inicio = novoNo

    #   deleteFirst
    def pop(self):
        no_removido = self._inicio
        # Verifica se ta vazia
        if not self.isVazia():
            # Verifica se tem apenas 1 elemento:
            #    - Se tiver não precisa mexer no depois do inicio, afinal ele não existe
            if no_removido._prox is None:
                pass

            else:
                # Retirando o ant do segundo (depois do inicio), transformando em None. Afinal ele se tornará o primeiro
                no_removido._prox._ant = None
            self._inicio = self._inicio._prox

        return no_removido

    # Definindo o print da PILHA
    def __str__(self):
        return "Pilha: " + super().__str__()

if __name__ == "__main__":
    # Inserindo dados na fila
    l = [4, 7, 17, 87]
    pilha = Pilha()

    print(f"\nINSERT FIRST\n")
    for i in l:
        pilha.push(i)
        print(f"{pilha}")

    print(f"\nDELETE FIRST\n")
    for _ in range(len(l)):
        print(f"{pilha}")
        print("Dado Removido: ", pilha.pop())
    print(f"{pilha}")