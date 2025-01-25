from Est_Dados.aLista_2ENC_DIN import Lista_2ENC

class Fila(Lista_2ENC):
    # Inserir no Final  --> Ja tem
    # Remover do Inicio

    def insert_Last(self, dado):
        self.insertLast(dado)

    def deleteFirst(self):
        #Verifica se ta vazia
        if not self.isVazia():
            # Verifica se tem apenas 1 elemento:
            #   - 1 ELEMENTO:
            #       Removendo ele o inicio o e o FIM tem q receber None
            if self._inicio._prox == None:
                self._fim = None

            else:
                # Retirando o anterior do segundo, transformando em None
                self._inicio._prox._ant = None
            self._inicio = self._inicio._prox

    # Definindo o print da FILA
    def __str__(self):
        return "Fila: " + super().__str__()

if __name__ == "__main__":
    # Inserindo dados na fila
    l = [4, 7, 17, 87]
    fila = Fila()

    print(f"\nINSERT LAST\n")
    for i in l:
        fila.insert_Last(i)
        print(f"{fila}")

    print(f"\nDELETE FIRST\n")
    for _ in range(len(l)):
        print(f"{fila}")
        fila.deleteFirst()
    print(f"{fila}")