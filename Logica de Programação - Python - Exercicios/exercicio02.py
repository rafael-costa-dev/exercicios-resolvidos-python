#Faça um algoritmo para calcular o estoque médio de uma peça

# Entrada de dados
quantidade_minima = int(input('Digite quantidade mínima: '));
quantidade_maxima = int(input('Digite quantidade máxima: '));

# Processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2

# Saída de dados
print('O estoque médio é de: ',estoque_medio);
