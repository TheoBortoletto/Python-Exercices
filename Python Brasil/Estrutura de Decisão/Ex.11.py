print("\n\t Exercício 11 \n")

'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
 e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo 
o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, 
informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = int (input("Digite seu salário: "))
print("\n")

if salario <= 280:

    ajustevinte = (salario * 0.2) + salario
    valoraumento = salario * 0.2

    print("Seu salário antes do reajuste era de: R$", salario)
    print("O percentual de aumento do seu salário foi de: 20%")
    print("O valor do aumento é de: R$", valoraumento)
    print("Seu salário após o aumento é de: R$", ajustevinte, "\n")

if salario > 280 and salario <= 700:

    ajustequinze = (salario * 0.15) + salario
    valoraumento = salario * 0.15

    print("Seu salário antes do reajuste era de: R$", salario)
    print("O percentual de aumento do seu salário foi de: 15%")
    print("O valor do aumento é de: R$", valoraumento)
    print("Seu salário após o aumento é de: R$", ajustequinze, "\n")

if salario > 700 and salario <= 1500:

    ajustedez = (salario * 0.10) + salario
    valoraumento = salario * 0.10

    print("Seu salário antes do reajuste era de: R$", salario)
    print("O percentual de aumento do seu salário foi de: 10%")
    print("O valor do aumento é de: R$", valoraumento)
    print("Seu salário após o aumento é de: R$", ajustedez, "\n")
