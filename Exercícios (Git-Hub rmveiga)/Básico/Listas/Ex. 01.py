print("\n\t Exercício 1 \n")

'''Desenvolva um programa que armazene 
quatro notas em uma lista e que apresente: 
média final, a maior nota e a menor nota'''

notas = []
cont = 1

while cont <= 4:
    Notas = float (input("Informe a sua nota: "))
    notas.append(Notas)
    cont += 1
    
media = sum(notas) / 4

print("\nNotas: ", notas, "\n")
print("Média: ", media)
print("Nota maior: ", max(notas))
print("Menor nota: ", min(notas), "\n")
