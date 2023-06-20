print("\n\t Exercício 3 \n")

'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

i = 1
num = []

while i <= 4:
    num.append(float (input("Digite as notas: ")))
    i += 1

print("\nNota 1: ", num[0])
print("Nota 2: ", num[1])
print("Nota 3: ", num[2])
print("Nota 4: ", num[3])

media = sum(num) / 4

print("\nMédia das notas: ", media)
