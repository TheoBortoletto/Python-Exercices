print("\n\t Exercício 5 \n")

'''Faça um programa para a leitura de duas notas parciais de um aluno.
   O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float (input("Digite o valor da primeira prova: "))
nota2 = float (input("Digite o valor da segunda prova: ")) 

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Sua média é:", media, "você foi aprovado. \n")

if media < 7:
    print("Sua média é:", media, "você foi reprovado. \n")

if media == 10:
    print("Sua média é:", media, "aprovado com Distinção. \n")