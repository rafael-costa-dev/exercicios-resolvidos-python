# Faça um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês

# Entrada de dados
valorHora = float(input('Digite seu valor hora aqui: '));
horasTrabalhadas = float(input('Digite quantas horas trabalhou: '));

# Processamento de dados
salario = valorHora * horasTrabalhadas;

# Saida de dados
print('Seu salário no mês é de R$:',salario);