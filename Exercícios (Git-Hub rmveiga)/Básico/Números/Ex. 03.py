print("\n\t Exercício 3 \n")

'''Desenvolva um programa que leia quatro notas e que apresente a média final'''

notas = []
cont = 1

while cont <= 4:
    Notas = float (input("Digite a sua nota: "))
    notas.append(Notas)
    cont += 1
    
media = sum(notas) / len(notas)

print("\nMédia: ", media, "\n")