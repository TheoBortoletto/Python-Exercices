print("\n\t - Exercício 1: \n")

''' 1) Para ser aprovado em uma disciplina o aluno precisa obter média final maior ou igual a 7,00.
Considere que em uma determinada disciplina ele realiza 3 atividades com os seguintes pesos:

Prova – peso 45%, 
Projeto – peso 25%,
Atividades – peso 30%.

Faça um programa para receber o nome da disciplina, as notas que o aluno obteve em cada atividade, 
calcule e mostre a média final e o resultado: Aprovado ou Reprovado.'''


disc = str (input("Nome da disciplina: "))
print("\n")

prova = float (input("Sua nota na prova: "))
projeto = float (input("Sua nota no projeto: "))
ativ = float (input("Sua nota nas atividades: "))

print("\n")

prova = prova * 0.45
projeto = projeto * 0.25
ativ = ativ * 0.3

media = (prova + projeto + ativ)

if media >= 7:
    print("Sua média é", media, "você está aprovado.")
else:
    print("Sua média é:", media, "você foi reprovado.")
    