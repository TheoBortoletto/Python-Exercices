print("\n\t Exercício 3 \n")

'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = str (input("Informe o seu nome: "))
while len(nome) <= 3:
    nome = str (input("Informe o seu nome: "))

idade = int (input("Informe a sua idade: "))
while idade > 150 or idade < 0:
    idade = int (input("Informe a sua idade: "))

salario = float (input("Informe o seu salário: "))
while salario <= 0:
    salario = float (input("Informe o seu salário: "))

sex = str (input("Informe a inicial do seu sexo: "))
while sex != "f" and sex != "m":
    sex = str (input("Informe a inicial do seu sexo: "))

estadoC = str (input("Informe a inicial do seu Estado Civil: "))
while estadoC != "s" and estadoC != "c" and estadoC != "v" and estadoC != "d":
    estadoC = str (input("Informe a inicial do seu Estado Civil: "))

