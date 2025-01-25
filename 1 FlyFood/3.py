import matplotlib.pyplot as plt

# Dados
pontos_entrega = [5, 6, 7, 8, 9, 10, 11, 12]
tempos = [0.001, 0.004, 0.026, 0.229, 2.28, 25.3, 298.11, 3830.84]

# Criar o gráfico
plt.figure(figsize=(6, 7))
plt.plot(pontos_entrega, tempos, marker='o', linestyle='-', color='b', label='Tempo vs Pontos de Entrega')

# Configurações do gráfico
plt.title('Tempo de Execução vs Pontos de Entrega\n Ryzen 5 1600af', fontsize=14)
plt.xlabel('Pontos de Entrega', fontsize=12)
plt.ylabel('Tempo (segundos)', fontsize=12)
plt.yscale('log')  # Escala logarítmica para melhor visualização dos tempos
plt.grid(True, which="major", linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

# Exibir o gráfico
plt.show()