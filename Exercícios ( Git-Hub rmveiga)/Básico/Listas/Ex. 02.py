print("\n\t Exercício 2 \n")

'''Desenvolva um programa que armazene quatro notas 
em uma lista e que apresente a média final. Caso a 
média seja igual ou superior a 7, apresentar a mensagem 
"APROVADO", caso contrário, armazenar a nota da prova 
final e recalcular a média. Caso a nova média seja 
igual superior a 5, apresentar a mensagem "APROVADO", 
caso contrário, apresentar a mensagem "REPROVADO"'''


notas = []
cont = 1

while cont <= 4:
    Notas = float (input("Digite a sua nota: "))
    notas.append(Notas)
    cont += 1
print("\n")
media = sum(notas) / 4

if media >= 7:
    print("Sua média é", media, "você foi aprovado.")
else:
    print("Sua média é", media, "você foi reprovado.")