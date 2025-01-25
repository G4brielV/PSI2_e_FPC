import matplotlib.pyplot as plt
import pandas as pd

# Dados
pontos_entrega = [5, 6, 7, 8, 9, 10, 11, 12]
tempos = [0.001, 0.004, 0.026, 0.229, 2.28, 25.31, 298.11, 3830.84]

# Criar DataFrame
dados = {
    "Pontos de Entrega": [int(p) for p in pontos_entrega],
    "Tempo (segundos)": tempos
}
tabela = pd.DataFrame(dados)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.axis('off')  # Remover os eixos

table = plt.table(
    cellText=tabela.values,
    colLabels=tabela.columns,
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]  # Ajusta a posição e o tamanho da tabela
)

# Estilo da tabela
table.auto_set_font_size(False)
table.set_fontsize(12)
table.auto_set_column_width(col=list(range(len(tabela.columns))))

# Exibir o gráfico
plt.show()
