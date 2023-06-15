print("\n\t Exercicío 14 \n")

'''Faça um programa que lê as duas notas parciais obtidas por um aluno
 numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
 de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0            A
  Entre 7.5 e 9.0             B
  Entre 6.0 e 7.5             C
  Entre 4.0 e 6.0             D
  Entre 4.0 e zero            E'''

p1 = float (input("Digite a nota da primeira prova: "))
p2 = float (input("Digite a nota da segunda prova: "))

media = (p1 + p2) / 2

print("\nMédia:", media)

if media >= 9.0 and media <= 10.0:
    print("Conceito - A")

if media >= 7.5 and media < 9.0:
    print("Conceito - B")

if media >= 6.0 and media < 7.5:
    print("Conceito - C")

if media >= 4.0 and media < 6.0:
    print("Conceito - D")

if media < 4.0:
    print("Conceito - E")

print("\n")