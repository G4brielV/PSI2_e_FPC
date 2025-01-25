from Est_Dados.aLista_2ENC_DIN import Lista_2ENC

class Fila(Lista_2ENC):
    # Inserir no Final  --> Ja tem
    # Remover do Inicio

    def insert_Last(self, dado):
        self.insertLast(dado)

    def deleteFirst(self):
        no_removido = self._inicio
        #Verifica se ta vazia
        if not self.isVazia():
            # Verifica se tem apenas 1 elemento:
            #   - 1 ELEMENTO:
            #       Removendo ele o inicio o e o FIM tem q receber None
            if no_removido._prox == None:
                self._fim = None

            else:
                # Retirando o anterior do segundo, transformando em None
                no_removido._prox._ant = None
            self._inicio = self._inicio._prox

        return no_removido
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
        print("Dado Removido: ",fila.deleteFirst())
    print(f"{fila}")